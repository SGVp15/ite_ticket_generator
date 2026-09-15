import itertools
from pathlib import Path

COUNT_QUESTIONS_IN_TICKET = 10

LOG_FILE = './log.txt'

COURSE_NUMBER = {
    'ITIL4FC': '01',
    'CobitC': '02',
    'BAFC': '03',
    'BASRMC': '04',
    'SCMC': '05',
    'CPIC': '06',
    'ICSC': '07',
    'ITAMC': '08',
    'ITHRC': '09',
    'OPSC': '10',
    'RCVC': '11',
    'RISKC': '12',
    'SOA4C': '13',
    'SYSAC': '14',
    'SCM_T': '15',
}

FULL_NAME_COURSE = {
    'ITIL4FC': 'ITIL 4 Основы сервис-менеджмента',
    'CobitC': 'Основы Cobit 2019',
    'BAFC': 'Основы бизнес-анализа',
    'SCMC': 'SCMC',
    'BASRMC': 'Бизнес-анализ. Управление требованиями к ПО',
    'OPSC': 'OPSC',
    'SCM_T': '',

}

PATH_QUESTIONS = Path('data') / 'input'
PATH_QUESTIONS.mkdir(exist_ok=True,parents=True)

FILE_XLSX = {
    'ITIL4FC': PATH_QUESTIONS / 'ITIL4FC.xlsx',
    'CobitC': PATH_QUESTIONS / 'CobitС.xlsx',
    'BAFC': PATH_QUESTIONS / 'BAFC.xlsx',
    'BASRMC': PATH_QUESTIONS / 'BASRMC.xlsx',
    'ICSC': PATH_QUESTIONS / 'ICSC.xlsx',
    'RCVC': PATH_QUESTIONS / 'RCVC.xlsx',
    'SCMC': PATH_QUESTIONS / 'SCMC.xlsx',
    'CPIC': PATH_QUESTIONS / 'CPIC.xlsx',
    'OPSC': PATH_QUESTIONS / 'OPSC.xlsx',

    # 'SCM_T': PATH_QUESTIONS / 'SCM_T.xlsx',
    'SCM_T': PATH_QUESTIONS / 'Тестовые вопросы SCM v.1.0.4.xlsx',
}

DOCX_TEMPLATE = './Шаблон экзамена.docx'

MAP_EXCEL = {
    'Уровень по Блуму': 'D',
    'Код вопроса': 'I',
    'Блок вопросов': 'J',
    'Действующий 1-да, 0-нет': 'L',
    'Версия': 'M',
    'Раздел курса': 'E'
}

MIX_ANSWER = list(itertools.permutations('1234'))

# Папка для выгрузки билетов
DIR_OUT = Path('./data') / 'out'
DIR_OUT.mkdir(exist_ok=True,parents=True)
