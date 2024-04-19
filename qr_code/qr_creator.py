import qrcode

from config import course_number


def create_qrcode(text: str, filename: str):
    img = qrcode.make(text)
    img.save(filename)


def get_qrcode_text_from_ticket(questions: dict) -> str:
    s = f"{course_number[questions[0].exam]}"
    # 'num_question': num_question,
    # 'category': category,
    # 'version': version,
    for q in questions:
        s += f"{q.num_question:03d}{q.category:02d}{q.version:02d}{q.mix_num:02d}"
    return s
