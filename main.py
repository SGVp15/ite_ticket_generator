import json
import os
import random
import re
import openpyxl

from config import map_excel, mix_aswer, dir_out, file_xlsx
from ispring import create_excel_file_for_ispring
from Question import Question


def create_folders(name):
    os.makedirs(f'{dir_out}/{name}/json', exist_ok=True)
    os.makedirs(f'{dir_out}/{name}/pdf', exist_ok=True)
    os.makedirs(f'{dir_out}/{name}/docx', exist_ok=True)


def read_excel(excel, page_name, column, row):
    sheet_ranges = excel[page_name]
    return str(sheet_ranges[f'{column}{row}'].value).strip()


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

    # file_json = os.path.join(path_questions, f'{exam}.json')
    # with open(file_json, 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(all_questions))
    return all_questions


def get_num_question_category_version(s) -> (int, int, int):
    s = s.split('.')
    try:
        num_question = int(s[1])
        category = int(s[2])
        version = int(s[3])
        return num_question, category, version
    except (IndexError, ValueError):
        return 0, 0, 0


def create_new_ticket(questions: [Question]) -> [Question]:
    ticket = []
    box_question = []
    while len(ticket) < 30 and len(questions) > 0:
        max_len = max(0, len(questions) - 1)
        n = random.randint(0, max_len)
        question = questions[n]
        if question.box_question == 'None' or question.box_question not in box_question:
            box_question.append(question.box_question)
            ticket.append(question)
        del questions[n]

    # добавить перемешивание правило перемешивания 0-23 в отдельное поле
    for q in ticket:
        q.mix_num = random.randint(0, 23)
        q.mix = mix_aswer[q.mix_num]
        q = mix_value(q)
        q.Answer = f"A: {q.answer_doc_a}\n\n" \
                   f"B: {q.answer_doc_b}\n\n" \
                   f"C: {q.answer_doc_c}\n\n" \
                   f"D: {q.answer_doc_d}\n\n"
    # l = random.choices(ascii_lowercase, k=5)
    # create_json(ticket=ticket, name=name)
    return ticket


#   перемешать варианты ответов
def mix_value(q: Question) -> Question:
    keys = ['A', 'B', 'C', 'D']
    __temp_dict = {}
    q.right_answer = q.ans_a
    for i in range(len(q.mix)):
        if q.mix[i] == '1':
            __temp_dict[keys[i]] = q.ans_a
        elif q.mix[i] == '2':
            __temp_dict[keys[i]] = q.ans_b
        elif q.mix[i] == '3':
            __temp_dict[keys[i]] = q.ans_c
        elif q.mix[i] == '4':
            __temp_dict[keys[i]] = q.ans_d

    q.answer_doc_a = __temp_dict[keys[0]]
    q.answer_doc_b = __temp_dict[keys[1]]
    q.answer_doc_c = __temp_dict[keys[2]]
    q.answer_doc_d = __temp_dict[keys[3]]
    return q


def create_txt(ticket, name):
    with open(file=name + '.txt', mode='w', encoding='utf-8') as f:
        for q in ticket:
            f.write(f"{q['id_question']}\t{q['right_answer']}\t{q['mix']}\t{q['category']}\n".capitalize())

    num = re.findall(r"\d+", name)
    # print(num[0])
    with open(file=name + '_to_excel.txt', mode='w', encoding='utf-8') as f:
        f.write(f'{num[0]}\t\n')
        for q in ticket:
            f.write(f"{q['right_answer']}\t{q['category']}\n".capitalize())


def set_to_json(obj, file_name):
    with open(f'{file_name}.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(obj))


def get_from_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
    return obj


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


if __name__ == '__main__':
    exams = []
    exams.append('ITIL4FC')
    exams.append('RCVC')
    exams.append('CPIC')
    exams.append('COBIT ICSC')
    exams.append('CobitC')
    exams.append('BAFC')
    exams.append('BASRMC')

    for exam in exams:
        print(f'\n{exam}[  create_new_tickets  ]')
        create_excel_file_for_ispring(get_all_questions_from_excel_file(exam))

        # create_folders(exam)
        # os.chdir(f'./{dir_out}/{exam}')
        # create_new_tickets(exam)
    #
    # print('\n[  convert_docx_to_pdf  ]')
    # for exam in exams:
    #     os.chdir(f'{dir_out}/{exam}')
    #     docx_files = set([x[:-5] for x in os.listdir('./') if x.endswith('.docx')])
    #     pdf_files = set([x[:-4] for x in os.listdir('./') if x.endswith('.pdf')])
    #     docx_files = docx_files - pdf_files
    #     for docx in docx_files:
    #         convert_docx_to_pdf(docx)
    #         print(docx)
    #     all_in_one_excel()
    #     os.chdir(f'../../')

    # print('\n[  all_in_one_excel  ]')
    # for exam in exams:
    #     os.chdir(f'{dir_out}/{exam}')
    #     all_in_one_excel()
