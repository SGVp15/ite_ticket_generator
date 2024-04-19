class Ticket:
    def __init__(self, ticket_name, exam_name, questions):
        self.ticket_name = ticket_name
        self.exam_name = exam_name
        self.questions = questions
        self.word_path_file = ''
        self.file_qrcode = ''
        self.file_qrcode_exam_num = ''
