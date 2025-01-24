import qrcode

from config import course_number
from ticket_.ticket import Ticket


def create_qrcode(text: str, filename: str):
    img = qrcode.make(text)
    img.save(filename)


def get_qrcode_text_from_ticket(ticket: Ticket) -> str:
    s = f"{course_number[ticket.exam_name]}"
    for q in ticket.questions:
        s += f"{int(q.num_question):03d}"
        s += f"{int(q.category):02d}"
        s += f"{int(q.version):02d}"
        s += f"{int(q.mix_num):02d}"
    return s
