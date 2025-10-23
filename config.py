import os

COUNT_QUESTIONS_IN_TICKET = 30

LOG_FILE = './log.txt'

COURSE_NUMBER = {
    'ITIL4FC': '01',
    'CobitC': '02',
    'BAFC': '03',
    'BASRMC': '04',
    'SCMC': '05',

    'SCM_T': '06',
}

FULL_NAME_COURSE = {
    'ITIL4FC': 'ITIL 4 Основы сервис-менеджмента',
    'CobitC': 'Основы Cobit 2019',
    'BAFC': 'Основы бизнес-анализа',
    'SCMC': 'SCMC',
    'BASRMC': 'Бизнес-анализ. Управление требованиями к ПО',

    'SCM_T': 'SCM_T',

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

MIX_ASWER = [
    '1234',
    '1243',
    '1324',
    '1342',
    '1423',
    '1432',
    '2134',
    '2143',
    '2314',
    '2341',
    '2413',
    '2431',
    '3124',
    '3142',
    '3214',
    '3241',
    '3412',
    '3421',
    '4123',
    '4132',
    '4213',
    '4231',
    '4312',
    '4321',
]

# Папка для выгрузки экзаменов
DIR_OUT = './data/out'
