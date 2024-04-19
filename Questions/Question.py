import random
from string import ascii_lowercase, ascii_uppercase, digits

from config import mix_aswer
from utils.utils import mix_value


class Question:
    def __init__(self,
                 id_question,
                 text_question,
                 ans_a,
                 ans_b,
                 ans_c,
                 ans_d,
                 box_question,
                 num_question,
                 category,
                 version,
                 exam, ):
        self.id_question: str = id_question
        self.text_question: str = text_question
        self.ans_a: str = ans_a
        self.ans_b: str = ans_b
        self.ans_c: str = ans_c
        self.ans_d: str = ans_d
        self.box_question: str = box_question
        self.num_question: int = num_question
        self.category: str = category
        self.version: int = version
        self.exam: str = exam

        self.mix: str = ''
        self.answer_doc_a: str = ''
        self.answer_doc_b: str = ''
        self.answer_doc_c: str = ''
        self.answer_doc_d: str = ''

        self.right_answer: str = ''


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
