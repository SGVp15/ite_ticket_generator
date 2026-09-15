import os
import random
import re
from copy import deepcopy
from pathlib import Path
from string import ascii_uppercase, digits

from Questions.question import Question
from config import DIR_OUT, FULL_NAME_COURSE


class Ticket:
    def __init__(self, exam_name: str, questions: [Question]):
        self.total_count_of_questions = len(questions)
        self.exam_name = exam_name
        self.full_name_course = FULL_NAME_COURSE[exam_name]
        self.ticket_name = ''
        self.create_random_name_ticket()
        self.questions = deepcopy(questions)
        self.dir_out = Path(DIR_OUT) / self.exam_name
        self.word_path_file = Path(self.dir_out) / 'docx' / f'{self.ticket_name}.docx'
        self.file_qrcode = Path(self.dir_out) / f'{self.ticket_name}_exam_num.png'
        self.file_qrcode_exam_num = Path(self.dir_out) / f'{self.ticket_name}.docx'

    def create_random_name_ticket(self):
        self.ticket_name = f'{self.exam_name}_'
        rand = random.choices(ascii_uppercase, k=3)
        self.ticket_name += ''.join(rand)
        rand = random.choices(digits, k=2)
        self.ticket_name += ''.join(rand)


def create_txt(ticket: Ticket):
    os.makedirs(f'{DIR_OUT}/{ticket.exam_name}', exist_ok=True)
    with open(file=DIR_OUT / ticket.exam_name / f'{ticket.ticket_name}.txt', mode='w', encoding='utf-8') as f:
        f.write("""Пробный экзамен 
Выбор одного ответа из четырех вариантов ответа

Инструкции
 
1. Необходимо ответить на все 10 вопросов.
2. На каждый вопрос есть только один правильный ответ.
3. Вам нужно правильно ответить, как минимум, на 7 вопросов, чтобы успешно сдать тест.
4. У вас есть 45 минут, чтобы пройти этот тест.
5. Использование других справочных материалов не допускаются.


""")
        for i, q in enumerate(ticket.questions):
            q: Question
            # f.write(f"{'\t'.join([q.id_question, q.right_answer, q.mix, str(q.num_category), q.category])}\n")
            f.write(f"{i + 1}). {q.text_question}\n\n"
                    f"\tA. {q.show_answer_a}\n"
                    f"\tB. {q.show_answer_b}\n"
                    f"\tC. {q.show_answer_c}\n"
                    f"\tD. {q.show_answer_d}\n"
                    f"\n\n")

    # num = re.findall(r"\d+", ticket.ticket_name)
    # with open(file=f'{DIR_OUT}/{ticket.exam_name}/{ticket.ticket_name}_to_excel.txt', mode='w', encoding='utf-8') as f:
    #     f.write(f'{num[0]}\t\n')
    #     for q in ticket.questions:
    #         q: Question
    #         f.write(f"{'\t'.join([q.right_answer, str(q.num_category)])}\n")


def create_gift(ticket: Ticket):
    def replase_(s):
        s = re.sub('=', '\=', s)
        s = re.sub('~', '\~', s)
        return s

    with open(file=f'{DIR_OUT}/{ticket.exam_name}/{ticket.ticket_name}_gift.txt', mode='w', encoding='utf-8') as f:
        s = ''
        for i, q in enumerate(ticket.questions):
            q: Question
            s += f'$CATEGORY: $module$/top/{q.category}\n\n'
            s += (f'::Вопрос {i + 1}::{q.text_question}{{\n'
                  f'\t={replase_(q.ans_a)}\n'
                  f'\t~{replase_(q.ans_b)}\n'
                  f'\t~{replase_(q.ans_c)}\n'
                  f'\t~{replase_(q.ans_d)}\n'
                  f'}}\n\n'
                  )
        f.write(s)

    num = re.findall(r"\d+", ticket.ticket_name)
    with open(file=f'{DIR_OUT}/{ticket.exam_name}/{ticket.ticket_name}_to_excel.txt', mode='w', encoding='utf-8') as f:
        f.write(f'{num[0]}\t\n')
        for q in ticket.questions:
            f.write(f"{'\t'.join([q.right_answer, str(q.num_category)])}\n")
