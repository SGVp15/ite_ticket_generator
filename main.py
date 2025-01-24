import os
import re

import docx2pdf

from Excel.excel import get_all_questions_from_excel_file
from Questions.question import create_new_ticket
from Word.doc_ticket import create_docx
from config import DIR_OUT
from ticket_.ticket import Ticket
from utils.utils import create_folders


def create_txt(ticket: Ticket):
    with open(file=f'{DIR_OUT}/{ticket.exam_name}/{ticket.ticket_name}.txt', mode='w', encoding='utf-8') as f:
        for q in ticket.questions:
            f.write(f"{'\t'.join([q.id_question, q.right_answer, q.mix, q.category])}\n".capitalize())

    num = re.findall(r"\d+", ticket.ticket_name)
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
                exam_name=exam
            )
            create_txt(ticket=ticket)
            create_docx(ticket=ticket)

        print('\n[  convert_docx_to_pdf  ]')
        docx_files = set([x[:-5] for x in os.listdir(f'./{DIR_OUT}/{exam}/docx') if x.endswith('.docx')])
        pdf_files = set([x[:-4] for x in os.listdir(f'./{DIR_OUT}/{exam}/pdf') if x.endswith('.pdf')])
        docx_files = docx_files - pdf_files
        for name in docx_files:
            docx = os.path.join(DIR_OUT, exam, 'docx', f'{name}.docx')
            pdf = os.path.join(DIR_OUT, exam, 'pdf', f'{name}.pdf')
            docx2pdf.convert(docx, pdf)
            print(docx)
