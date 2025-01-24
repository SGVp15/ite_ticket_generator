import random
from string import ascii_lowercase

from config import MIX_ASWER


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
        self.show_answer_a: str = ''
        self.show_answer_b: str = ''
        self.show_answer_c: str = ''
        self.show_answer_d: str = ''

        self.right_answer: str = ''
        self.answer_text: str = self.replace_answer_text()

    def replace_answer_text(self):
        self.answer_text = f"A: {self.show_answer_a}\n\n" \
                           f"B: {self.show_answer_b}\n\n" \
                           f"C: {self.show_answer_c}\n\n" \
                           f"D: {self.show_answer_d}\n\n"
        return self.answer_text

    def mix_answers(self):
        if self.mix:
            keys = ['A', 'B', 'C', 'D']
            temp_dict = {}
            self.right_answer = self.ans_a
            for i, k in enumerate(keys):
                if self.mix[i] == '1':
                    temp_dict[k] = self.ans_a
                elif self.mix[i] == '2':
                    temp_dict[k] = self.ans_b
                elif self.mix[i] == '3':
                    temp_dict[k] = self.ans_c
                elif self.mix[i] == '4':
                    temp_dict[k] = self.ans_d

            self.show_answer_a = temp_dict[keys[0]]
            self.show_answer_b = temp_dict[keys[1]]
            self.show_answer_c = temp_dict[keys[2]]
            self.show_answer_d = temp_dict[keys[3]]
        self.replace_answer_text()


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
        q.mix = MIX_ASWER[q.mix_num]
        q.mix_answers()

    return ticket
