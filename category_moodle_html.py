import re

with open(f'./data/html/1.html', mode='r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<br[ /]*>\s+', ' ', text)

rows = [line for line in text.split('\n') if re.search('div id="question-', line)]
i = 0
for row in rows:
    try:
        ball = re.findall('<div class="grade">Баллов:( .* )из 1,00</div>', row)[0]
        ball = ball.strip()
        ball = re.sub(r',\d+', '', ball)
        ball = int(ball)
    except Exception as e:
        print(f'{row}\n\n {e}\n')
        pass
    try:
        q = re.findall('<div class="qtext"><div class="clearfix">([^/]*)</div>', row)[0]
    except Exception as e:
        # print(f'{row}\n\n')
        pass
    i += 1
    print(f'{i} {q}\t[{ball}]')
