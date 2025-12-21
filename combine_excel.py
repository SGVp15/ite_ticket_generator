import glob
import re

import openpyxl


def combine_excel_files_no_pandas(output_filename="combined_data_openpyxl.xlsx"):
    """
    Находит все файлы .xlsx в текущей директории и объединяет данные со всех
    листов каждого файла в один новый файл Excel с использованием openpyxl.
    """

    # Шаг 1: Поиск всех файлов Excel (исключая будущий выходной файл)
    all_files = glob.glob("data/input/*.xlsx")
    excel_files = [f for f in all_files if f != output_filename]

    if not excel_files:
        print("❌ Файлы Excel (.xlsx) не найдены в текущей директории.")
        return

    print(f"✅ Найдено {len(excel_files)} файлов Excel для объединения: {excel_files}")

    # Создаем новую рабочую книгу (workbook) и лист для объединенных данных
    new_wb = openpyxl.Workbook()
    # Удаляем лист по умолчанию, который создается автоматически
    default_sheet = new_wb.active
    new_wb.remove(default_sheet)

    # Создаем новый лист для записи объединенных данных
    combined_ws = new_wb.create_sheet(title="Combined_Data")

    # Переменная для отслеживания текущей строки записи
    current_row = 1
    # Флаг для записи заголовков (должны быть записаны только один раз)
    headers_written = False

    # Шаг 2: Чтение данных из каждого файла и запись в новый лист
    for filename in excel_files:
        try:
            print(f"📖 Чтение файла: {filename}...")

            # Загружаем рабочую книгу
            wb = openpyxl.load_workbook(filename, data_only=True)

            for sheet_name in wb.sheetnames:
                print(f"   -> Чтение листа: {sheet_name}")
                ws = wb[sheet_name]

                # Итерируемся по всем строкам на листе
                for row_index, row in enumerate(ws.iter_rows()):
                    # Извлекаем значения ячеек для текущей строки
                    row_data = [cell.value for cell in row]

                    # Создаем дополнительные ячейки для источника
                    source_info = [filename, sheet_name]

                    # Если это первая строка листа (заголовки)
                    if row_index == 0:
                        if not headers_written:
                            # Записываем заголовки + заголовки источника
                            combined_ws.append(row_data + ["Source_File", "Source_Sheet"])
                            current_row += 1
                            headers_written = True
                        else:
                            # Пропускаем заголовки, если они уже записаны
                            continue

                            # Если это строка данных (не заголовки)
                    elif (row_index > 0
                          and re.match(r'^\d+.*', str(row_data[0]))
                          and row_data[4]
                    ):
                        # Записываем данные + информацию об источнике
                        combined_ws.append(row_data + source_info)
                        current_row += 1


        except Exception as e:
            print(f"⚠️ Ошибка при обработке файла {filename}: {e}")

    # Шаг 3: Сохранение объединенного файла
    if combined_ws.max_row == 1 and headers_written:
        print("⚠️ Данные, кроме заголовков, не были найдены или объединены.")
        # Если было записано только название листа и заголовки, файл может быть пустым, но мы его сохраним
    elif not headers_written:
        print("❌ Не удалось прочитать данные ни из одного файла. Выходной файл не будет создан.")
        return

    try:
        print(f"💾 Сохранение объединенных данных в {output_filename}...")
        new_wb.save(output_filename)
        print(f"🎉 Успешно! Все данные сохранены в файле '{output_filename}' на листе 'Combined_Data'.")

    except Exception as e:
        print(f"❌ Ошибка при сохранении выходного файла: {e}")


if __name__ == "__main__":
    # Укажи имя выходного файла
    combine_excel_files_no_pandas("Combined_Data_Result_NoPandas.xlsx")
