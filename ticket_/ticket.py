import os
import random
from copy import deepcopy
from string import ascii_uppercase, digits

from Questions.question import Question
from config import DIR_OUT


class Ticket:
    def __init__(self, exam_name: str, questions: Question):
        self.total_count_of_questions = len(questions)
        self.exam_name = exam_name
        self.ticket_name = ''
        self.create_random_name_ticket()
        self.questions = deepcopy(questions)
        self.dir_out = os.path.join(DIR_OUT, self.exam_name)
        self.word_path_file = os.path.join(self.dir_out, 'docx', f'{self.ticket_name}.docx')
        self.file_qrcode = os.path.join(self.dir_out, f'{self.ticket_name}_exam_num.png')
        self.file_qrcode_exam_num = os.path.join(self.dir_out, f'{self.ticket_name}.docx')

    def create_random_name_ticket(self):
        self.ticket_name = f'{self.exam_name}_'
        rand = random.choices(ascii_uppercase, k=3)
        self.ticket_name += ''.join(rand)
        rand = random.choices(digits, k=2)
        self.ticket_name += ''.join(rand)
