import os


def mkdir(path: str):
    os.makedirs(path, exist_ok=True)
