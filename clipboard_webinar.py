import random
import re
from string import ascii_letters, digits


def generator_password(k=10):
    password = random.choices(ascii_letters, k=k)
    password.extend(random.choices(digits, k=k))
    return ''.join(password)


def replace_string(s: str) -> str:
    rows = s.split('\n')
    out = []
    for row in rows:
        row = row.strip()
        try:
            email = re.findall(r'(\S*@\S*)', row)[0]
            row = re.sub(r'(\S*@\S*)', '', row)
            row = re.sub(r'\d+', '', row)

            row_eng = row.split('\t')
            name_eng = ''
            for w in row_eng:
                find = re.findall(r'([A-Za-z]+\s+[A-Za-z]+)', w)
                if len(find) > 0:
                    name_eng = find[0]

            row = re.sub(r'^\s+', '', row)
            row = row.split(' ')

            first_name = row[1]
            last_name = row[0]
            password = generator_password()
            login = re.sub(r'@.*', '', email)

            out.append(f'{last_name}\t{first_name}\t{login}\t{password}\t{email}\t\t\t\t{name_eng}\tОбучающийся\t22')
        except Exception:
            pass
    s = '\n'.join(out)
    return s
