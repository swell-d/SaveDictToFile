import codecs
import pathlib
from datetime import datetime


class SwPrint:
    __log = ''
    __debug = False
    __start_time = ''

    @classmethod
    def __init__(cls, debug=False):
        cls.__debug = debug
        cls.__start_time = datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M")

    @classmethod
    def print(cls, text, only_debug=False, end='\n'):
        if not cls.__debug and only_debug: return
        text = f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H:%M:%S")}  {str(text)}{end}'
        print(text, end='')
        cls.__log += text

    @classmethod
    def save_log_to_file(cls, prj_name='', path='C:\\Users\\Administrator\\Documents\\_python\\_logs\\'):
        full_path = f'{path}\\{cls.__start_time}_{prj_name}.txt'
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        with codecs.open(full_path, 'w', 'utf-8') as f:
            f.write(cls.__log)

    # def print(text, only_debug=False, end='\n'):
    #     SwPrint.print(text, only_debug, end)
