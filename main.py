import os
import re

from Excel.excel import get_all_questions_from_excel_file, all_in_one_excel
from Questions.question import create_new_ticket, create_random_name_ticket
from Word.doc_ticket import create_docx, convert_docx_to_pdf
from config import DIR_OUT
from ticket_.ticket import Ticket
from utils.utils import create_folders


def create_txt(ticket: Ticket):
    with open(file=f'{DIR_OUT}/{ticket.exam_name}/{ticket.ticket_name}.txt', mode='w', encoding='utf-8') as f:
        for q in ticket.questions:
            f.write(f"{'\t'.join([q.id_question, q.right_answer, q.mix, q.category])}\n".capitalize())

    num = re.findall(r"\d+", ticket.ticket_name)
    # print(num[0])
    with open(file=f'{DIR_OUT}/{ticket.exam_name}/{ticket.ticket_name}_to_excel.txt', mode='w', encoding='utf-8') as f:
        f.write(f'{num[0]}\t\n')
        for q in ticket.questions:
            f.write(f"{'\t'.join([q.right_answer, q.category])}\n".capitalize())


if __name__ == '__main__':
    exams = []
    # exams.append('SCMC')
    exams.append('ITIL4FC')

    for exam in exams:
        create_folders(exam)
        print(f'\n{exam}[  create_new_tickets  ]')
        all_questions = get_all_questions_from_excel_file(exam)
        for ticket_name in range(1):
            ticket = Ticket(
                questions=create_new_ticket(all_questions, min(30, len(all_questions))),
                exam_name=exam,
                ticket_name=create_random_name_ticket(exam)
            )
            create_txt(ticket=ticket)
            create_docx(ticket=ticket)

            # print('\n[  convert_docx_to_pdf  ]')
            # os.chdir(f'{DIR_OUT}/{exam}')
            # docx_files = set([x[:-5] for x in os.listdir('./') if x.endswith('.docx')])
            # pdf_files = set([x[:-4] for x in os.listdir('./') if x.endswith('.pdf')])
            # docx_files = docx_files - pdf_files
            # for docx in docx_files:
            #     convert_docx_to_pdf(docx)
            # print(docx)
            # all_in_one_excel()
            #
            # print('\n[  all_in_one_excel  ]')

            # all_in_one_excel()
