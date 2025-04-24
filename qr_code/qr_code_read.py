import os
import re

import cv2
from pyzbar import pyzbar

from config import MIX_ASWER, COURSE_NUMBER


def __a():
    for file in os.listdir('./qr/'):
        file = f'./qr/{file}'
        img = cv2.imread(file)
        # обнаружить и декодировать
        qrcodes = pyzbar.decode(img)
        data = qrcodes[0][0].decode("utf-8")

        course = data[:2]
        data = data[2:]
        q = []
        k = 9
        keys = ['A', 'B', 'C', 'D']
        with open(file[:-3] + 'txt', 'w') as f:
            for i in range(30):
                a = k * i
                num = int(data[a:a + 3])
                category = int(data[a + 3:a + 5])
                answer = MIX_ASWER[int(data[a + 7:a + 9])]
                answer = keys[answer.find('1')]
                version = int(data[a + 5:a + 7])

                f.write(f'{answer}\t{category}\n')

        print(course)


def uncoding(s: str):
    course = next((key for key, value in COURSE_NUMBER.items() if value == s[:2]), None)
    s = s[2:]
    k = 9
    keys = ['A', 'B', 'C', 'D']
    print(course)
    rows = re.findall(r'(.{9})', s)
    for i, row in enumerate(rows):
        num = int(row[:3])
        category = int(row[3:5])
        answer = MIX_ASWER[int(row[7:9])]
        answer = keys[answer.find('1')]
        version = int(row[5:7])
        print(f'{i + 1}\t{num=}\t{answer=}\t{category=}\t{version=}')
        # print(f'{i + 1}\t{answer}')


data = '01028050118009010104004010115017030100035060118049060110013020103007010108060060115044060116041060121043060102005010113056060117036060118021040105031060104002010109052060120008010100030060113014030120039060101042060119020040114032060121023040122037060102047060122045060116'
uncoding(data)
