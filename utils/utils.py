import json
import os

from Question import Question
from config import dir_out


def mkdir(path: str):
    os.makedirs(path, exist_ok=True)


def create_folders(name):
    os.makedirs(f'{dir_out}/{name}/json', exist_ok=True)
    os.makedirs(f'{dir_out}/{name}/pdf', exist_ok=True)
    os.makedirs(f'{dir_out}/{name}/docx', exist_ok=True)


def mix_value(q: Question) -> Question:
    keys = ['A', 'B', 'C', 'D']
    __temp_dict = {}
    q.right_answer = q.ans_a
    for i in range(len(q.mix)):
        if q.mix[i] == '1':
            __temp_dict[keys[i]] = q.ans_a
        elif q.mix[i] == '2':
            __temp_dict[keys[i]] = q.ans_b
        elif q.mix[i] == '3':
            __temp_dict[keys[i]] = q.ans_c
        elif q.mix[i] == '4':
            __temp_dict[keys[i]] = q.ans_d

    q.answer_doc_a = __temp_dict[keys[0]]
    q.answer_doc_b = __temp_dict[keys[1]]
    q.answer_doc_c = __temp_dict[keys[2]]
    q.answer_doc_d = __temp_dict[keys[3]]
    return q


def get_from_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
    return obj


def set_to_json(obj, file_name):
    with open(f'{file_name}.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(obj))
