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
