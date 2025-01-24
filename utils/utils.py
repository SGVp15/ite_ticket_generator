import json
import os

from config import DIR_OUT


def mkdir(path: str):
    os.makedirs(path, exist_ok=True)


def create_folders(name):
    os.makedirs(os.path.join(DIR_OUT, name, 'json'), exist_ok=True)
    os.makedirs(os.path.join(DIR_OUT, name, 'pdf'), exist_ok=True)
    os.makedirs(os.path.join(DIR_OUT, name, 'docx'), exist_ok=True)


def get_from_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
    return obj


def set_to_json(obj, file_name):
    with open(f'{file_name}.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(obj))
