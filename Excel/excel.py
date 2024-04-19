import os
import random

import openpyxl

from Questions.Question import Question
from config import file_xlsx, map_excel, path_questions


def get_all_questions_from_excel_file(exam: str) -> [Question]:
    file = file_xlsx[exam]
    wb = openpyxl.load_workbook(filename=f'{file}', data_only=True)
    page_name = wb.sheetnames
    page_name = str(page_name[0])
    col_id_question = map_excel['Код вопроса']
    col_box_question = map_excel['Блок вопросов']
    column_enable_question = map_excel['Действующий 1-да, 0-нет']

    column_a = 'a'
    column_main = 'b'

    all_questions = []
    num_q = 0

    i = 0
    while i < 20000:
        i += 1
        a = read_excel(wb, page_name, column_a, i + 1).lower()
        b = read_excel(wb, page_name, column_a, i + 2).lower()
        c = read_excel(wb, page_name, column_a, i + 3).lower()
        d = read_excel(wb, page_name, column_a, i + 4).lower()

        if a in ('a', 'а') and b in ('b', 'в') and c in ('c', 'с') and d == 'd':
            enable_question = read_excel(wb, page_name, column_enable_question, i)
            if enable_question:
                id_question = read_excel(wb, page_name, col_id_question, i)
                box_question = read_excel(wb, page_name, col_box_question, i)
                if box_question == 'None':
                    box_question = random.randint(200, 300_000_000_000)
                ans_a = read_excel(wb, page_name, column_main, i + 1)
                ans_b = read_excel(wb, page_name, column_main, i + 2)
                ans_c = read_excel(wb, page_name, column_main, i + 3)
                ans_d = read_excel(wb, page_name, column_main, i + 4)
                num_q += 1
                text_question = read_excel(wb, page_name, column_main, i)
                num_question, category, version = get_num_question_category_version(id_question)
                category = read_excel(wb, page_name, "D", i)
                all_questions.append(
                    Question(
                        id_question=id_question,
                        text_question=text_question,
                        ans_a=ans_a,
                        ans_b=ans_b,
                        ans_c=ans_c,
                        ans_d=ans_d,
                        box_question=box_question,
                        num_question=num_question,
                        category=category,
                        version=version,
                        exam=exam,
                    ))
            i += 3

    file_json = os.path.join(path_questions, f'{exam}.json')
    # with open(file_json, 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(all_questions))
    return all_questions


def read_excel(excel, page_name, column, row):
    sheet_ranges = excel[page_name]
    return str(sheet_ranges[f'{column}{row}'].value).strip()


def get_num_question_category_version(s) -> (int, int, int):
    s = s.split('.')
    try:
        num_question = int(s[1])
        category = int(s[2])
        version = int(s[3])
        return num_question, category, version
    except (IndexError, ValueError):
        return 0, 0, 0


class excel():
    def read_excel(excel, page_name, column, row):
        sheet_ranges = excel[page_name]
        return str(sheet_ranges[f'{column}{row}'].value)


def all_in_one_excel():
    excel = [x for x in os.listdir(f'./') if x.endswith('to_excel.txt')]
    # print(excel)

    out = ['' for _ in range(100)]
    for file in excel:
        with open(file, mode='r', encoding='utf-8') as f:
            s = f.read().split('\n')
            for i in range(len(s)):
                out[i] = out[i] + s[i] + '\t'
    with open(f'./all_excel.txt', mode='w', encoding='utf-8') as f:
        f.write('')
    with open(f'./all_excel.txt', mode='w', encoding='utf-8') as f:
        s = '\n'.join(out)
        f.write(s.strip())
