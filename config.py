import os

COUNT_QUESTIONS_IN_TICKET = 30

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
}

FULL_NAME_COURSE = {
    'ITIL4FC': 'ITIL 4 Основы сервис-менеджмента',
    'CobitC': 'Основы Cobit 2019',
    'BAFC': 'Основы бизнес-анализа',
    'SCMC': 'SCMC',
    'BASRMC': 'Бизнес-анализ. Управление требованиями к ПО',
    'OPSC': 'OPSC',

}

PATH_QUESTIONS = os.path.join(os.getcwd(), 'data', 'input')

FILE_XLSX = {
    'ITIL4FC': os.path.join(PATH_QUESTIONS, 'ITIL4FC.xlsx'),
    'CobitC': os.path.join(PATH_QUESTIONS, 'CobitС.xlsx'),
    'BAFC': os.path.join(PATH_QUESTIONS, 'BAFC.xlsx'),
    'BASRMC': os.path.join(PATH_QUESTIONS, 'BASRMC.xlsx'),
    'COBIT ICSC': os.path.join(PATH_QUESTIONS, 'COBIT ICSC.xlsx'),
    'RCVC': os.path.join(PATH_QUESTIONS, 'RCVC.xlsx'),
    'SCMC': os.path.join(PATH_QUESTIONS, 'SCMC.xlsx'),
    'CPIC': os.path.join(PATH_QUESTIONS, 'CPIC.xlsx'),
    'OPSC': os.path.join(PATH_QUESTIONS, 'OPSC.xlsx'),

    'SCM_T': os.path.join(PATH_QUESTIONS, 'SCM_T.xlsx'),
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

MIX_ASWER = list(itertools.permutations('1234'))

# Папка для выгрузки экзаменов
DIR_OUT = './data/out'
