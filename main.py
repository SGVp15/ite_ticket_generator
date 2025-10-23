import os

import docx2pdf

from Excel.excel import get_all_questions_from_excel_file
from Questions.question import create_new_ticket
from Word.doc_ticket import create_docx
from config import DIR_OUT, COUNT_QUESTIONS_IN_TICKET
from ticket_.ticket import Ticket, create_txt, create_gift
from utils.utils import create_folders


def main():
    exams = []
    # exams.append('SCMC')
    exams.append('ITIL4FC')
    # exams.append('SCM_T')

    for exam in exams:
        create_folders(exam)
        print(f'\n{exam}[  create_new_tickets  ]')
        all_questions = get_all_questions_from_excel_file(exam)
        for ticket_name in range(1):
            ticket = Ticket(
                questions=create_new_ticket(all_questions, min(COUNT_QUESTIONS_IN_TICKET, len(all_questions))),
                exam_name=exam
            )
            create_txt(ticket=ticket)
            create_gift(ticket=ticket)
            # create_docx(ticket=ticket)

        # print('\n[  convert_docx_to_pdf  ]')
        # docx_files = set([x[:-5] for x in os.listdir(f'./{DIR_OUT}/{exam}/docx') if x.endswith('.docx')])
        # pdf_files = set([x[:-4] for x in os.listdir(f'./{DIR_OUT}/{exam}/pdf') if x.endswith('.pdf')])
        # docx_files = docx_files - pdf_files
        # for name in docx_files:
        #     docx = os.path.join(DIR_OUT, exam, 'docx', f'{name}.docx')
        #     pdf = os.path.join(DIR_OUT, exam, 'pdf', f'{name}.pdf')
        #     docx2pdf.convert(docx, pdf)
        #     print(docx)


if __name__ == '__main__':
    for i in range(1):
        main()
