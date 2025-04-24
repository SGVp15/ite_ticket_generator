import qrcode

from config import COURSE_NUMBER
from ticket_.ticket import Ticket


def create_qrcode(text: str, filename: str):
    img = qrcode.make(text)
    img.save(filename)


def get_qrcode_text_from_ticket(ticket: Ticket) -> str:
    s = f"{COURSE_NUMBER[ticket.exam_name]}"
    for q in ticket.questions:
        s += f"{q.num_question:03d}"
        s += f"{q.category:02d}"
        s += f"{q.version:02d}"
        s += f"{q.mix_num:02d}"
    return s
