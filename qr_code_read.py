import cv2
from pyzbar import pyzbar

from config import mix_aswer
import os

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
            answer = mix_aswer[int(data[a + 7:a + 9])]
            answer = keys[answer.find('1')]
            version = int(data[a + 5:a + 7])

            f.write(f'{answer}\t{category}\n')

    print(course)
