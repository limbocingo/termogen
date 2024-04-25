from datetime import datetime


class Color:
    dark_gray = '\033[90m'
    indian_red = '\033[91m'
    indigo = '\033[94m'
    cadet_blue = '\033[96m'
    light_green = '\033[92m'
    corn_silk = '\033[93m'
    reset = '\033[0m'
    red = '\033[31m'
    dark_red = '\033[31;1m'


def log(value: str, color: str, prefix: str = 'NULL') -> str:
    print(f'{Color.indigo}{datetime.today()} {Color.dark_gray}[{
          color}{prefix}{Color.dark_gray}]{Color.reset} {value}')
