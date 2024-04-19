import os
import re

from Excel.excel import get_all_questions_from_excel_file, all_in_one_excel
from config import dir_out
from Word.doc_ticket import create_docx, convert_docx_to_pdf
from Questions.Question import create_new_ticket, create_names_tickets
from utils.utils import create_folders


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
