import os

LOG_FILE = './log.txt'

course_number = {'ITILFC': '01',
                 'CobitC': '02',
                 'BAFC': '03',
                 'BASRMC': '04',
                 'SCMC': '05'}

full_name_course = {'ITILFC': 'ITIL 4 Основы сервис-менеджмента',
                    'CobitC': 'Основы Cobit 2019',
                    'BAFC': 'Основы бизнес-анализа',
                    'SCMC': 'SCMC',
                    'BASRMC': 'Бизнес-анализ. Управление требованиями к ПО',
                    }

PATH_QUESTIONS = os.path.join(os.getcwd(), 'data', 'input')

file_xlsx = {'ITIL4FC': os.path.join(PATH_QUESTIONS, 'ITIL4FC.xlsx'),
             'CobitC': os.path.join(PATH_QUESTIONS, 'CobitС.xlsx'),
             'BAFC': os.path.join(PATH_QUESTIONS, 'BAFC.xlsx'),
             'BASRMC': os.path.join(PATH_QUESTIONS, 'BASRMC.xlsx'),
             'COBIT ICSC': os.path.join(PATH_QUESTIONS, 'COBIT ICSC.xlsx'),
             'RCVC': os.path.join(PATH_QUESTIONS, 'RCVC.xlsx'),
             'SCMC': os.path.join(PATH_QUESTIONS, 'SCMC.xlsx'),
             'CPIC': os.path.join(PATH_QUESTIONS, 'CPIC.xlsx'),
             }

docx_template = './Шаблон экзамена.docx'

map_excel = {
    'Уровень по Блуму': 'C',
    'Раздел курса': 'D',
    'Версия презентация': 'E',
    'Ссылка на презентацию': 'F',
    'Ссылка на источник': 'G',
    'Код вопроса': 'H',
    'Блок вопросов': 'I',
    'Пояснение': 'J',
    'Действующий 1-да, 0-нет': 'K',
    'Версия': 'L',
}

mix_aswer = ['1234',
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
             '4321']

# Папка для выгрузки экзаменов
dir_out = './data/out'
