import os
from copy import deepcopy

from Questions.question import Question
from config import DIR_OUT


class Ticket:
    def __init__(self, ticket_name: str, exam_name: str, questions: Question):
        self.total_count_of_questions = len(questions)
        self.ticket_name = ticket_name
        self.exam_name = exam_name
        self.questions = deepcopy(questions)
        self.dir_out = os.path.join(DIR_OUT, self.exam_name)
        self.word_path_file = os.path.join(self.dir_out, f'{self.ticket_name}.docx')
        self.file_qrcode = os.path.join(self.dir_out, f'{self.ticket_name}_exam_num.png')
        self.file_qrcode_exam_num = os.path.join(self.dir_out, f'{self.ticket_name}.docx')
