import os
import random
import time

import docx2pdf
from docx import Document
from docx.shared import Inches

from Questions.question import Question
from config import docx_template, full_name_course
from qr_code.qr_creator import create_qrcode, get_qrcode_text_from_ticket
from Word.replace import replace_docx_text
from ticket_.ticket import Ticket


def get_random_index_list_quest(list_quest, max_group):
    out = []
    # print([x - 1 for x in list_quest])
    for group in range(0, max_group):
        l = []
        for i, v in enumerate(list_quest):
            v1 = v - 1
            if v1 < len(out) or len(out) == 0:
                l.append(random.randint(0, v1))
            else:
                temp_l = []
                for o in out:
                    temp_l.append(o[i])
                n = 0
                while True:
                    n = random.randint(0, v1)
                    if n not in temp_l:
                        break
                l.append(n)
        out.append(l.copy())
    return out


def convert_docx_to_pdf(file):
    pdf = f'{os.getcwd()}/{file}.pdf'
    print(pdf)
    docx2pdf.convert(f'./{file}.docx', pdf)
    print(file)
    time.sleep(0.1)


def create_docx(ticket: Ticket):
    document = Document(docx_template)
    # replace_docx_text(document, old_text='Exam', new_text=ticket.exam)
    file_qrcode = f'{ticket.ticket_name}.png'
    file_qrcode_exam_num = f'{ticket.ticket_name}_exam_num.png'

    create_qrcode(text=ticket.ticket_name, filename=file_qrcode_exam_num)
    create_qrcode(text=get_qrcode_text_from_ticket(ticket), filename=file_qrcode)

    tables = document.tables
    p = tables[3].rows[0].cells[1].add_paragraph()
    r = p.add_run()
    r.add_picture(file_qrcode, width=Inches(2))

    p = tables[0].rows[0].cells[1].add_paragraph()
    r = p.add_run()
    r.add_picture(file_qrcode_exam_num, width=Inches(1))

    course = full_name_course[questions[1].exam]

    replace_docx_text(document, old_text='Code', new_text=name)
    replace_docx_text(document, old_text='Exam', new_text=questions[1]['exam'])
    replace_docx_text(document, old_text='Course', new_text=course)
    for i in range(30):
        try:
            replace_docx_text(document, old_text=f'Question_{i + 1}',
                              new_text=f'{i + 1}.\t' + questions[i].text_question)
            replace_docx_text(document, old_text=f'Answer_{i + 1}', new_text=questions[i].Answer)
        except IndexError:
            break
    document.save(f'{name}.docx')
