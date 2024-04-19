class Ticket:
    def __init__(self, ticket_name, exam_name, word_path_file, questions):
        self.ticket_name = ticket_name
        self.exam_name = exam_name
        self.word_path_file = word_path_file
        self.questions = questions
        self.file_qrcode = ''
        self.file_qrcode_exam_num = ''
