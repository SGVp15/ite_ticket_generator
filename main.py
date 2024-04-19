import os
import random
import re
from string import ascii_uppercase, digits, ascii_lowercase

from Excel.excel import get_all_questions_from_excel_file
from config import mix_aswer, dir_out
from Word.doc_ticket import create_docx, convert_docx_to_pdf
from Question import Question
from utils.utils import create_folders, mix_value


def create_new_ticket(questions: [Question], max_num_question: int) -> [Question]:
    ticket = []
    box_question = []
    while len(ticket) < max_num_question and len(questions) > 0:
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
    l = random.choices(ascii_lowercase, k=5)
    # create_json(ticket=ticket, name=name)
    return ticket


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


def create_names_tickets(exam: str, num) -> [str]:
    tickets_name = []
    for i in range(num):
        ticket_name = f'{exam}'
        ticket_name += f'{i:03d}'
        rand = random.choices(ascii_uppercase, k=3)
        ticket_name += ''.join(rand)
        rand = random.choices(digits, k=2)
        ticket_name += ''.join(rand)
        tickets_name.append(ticket_name)
    return tickets_name


if __name__ == '__main__':
    exams = []
    exams.append('SCMC')

    for exam in exams:
        print(f'\n{exam}[  create_new_tickets  ]')
        # create_excel_file_for_ispring(get_all_questions_from_excel_file(exam))
        all_questions = get_all_questions_from_excel_file(exam)

        create_folders(exam)
        os.chdir(f'./{dir_out}/{exam}')
        tickets_names = create_names_tickets(exam, num=5)

        # set_to_json(obj=ticket, file_name=f'{name}')
        # create_txt(ticket=ticket, name=f'{name}')
        for ticket_name in tickets_names:
            ticket = create_new_ticket(all_questions, 5)
            create_docx(questions=ticket, name=f'{ticket_name}')

    print('\n[  convert_docx_to_pdf  ]')
    for exam in exams:
        os.chdir(f'{dir_out}/{exam}')
        docx_files = set([x[:-5] for x in os.listdir('./') if x.endswith('.docx')])
        pdf_files = set([x[:-4] for x in os.listdir('./') if x.endswith('.pdf')])
        docx_files = docx_files - pdf_files
        for docx in docx_files:
            convert_docx_to_pdf(docx)
            print(docx)
        all_in_one_excel()
        os.chdir(f'../../')

    print('\n[  all_in_one_excel  ]')
    for exam in exams:
        os.chdir(f'{dir_out}/{exam}')
        all_in_one_excel()
