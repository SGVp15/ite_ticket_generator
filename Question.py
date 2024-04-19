from dataclasses import dataclass


@dataclass
class Question:
    id_question: str
    text_question: str
    ans_a: str
    ans_b: str
    ans_c: str
    ans_d: str
    box_question: str
    num_question: int
    category: str
    version: int
    exam: str

    mix: str
    answer_doc_a: str
    answer_doc_b: str
    answer_doc_c: str
    answer_doc_d: str

    right_answer: str
