from datetime import datetime
from pathlib import Path

from main.logg.level import Level


cwd = Path.cwd()


def log_message(filename: str, log_type: Level, msg):
    if not msg:
        raise Exception('Please inform a message')
    if not filename:
        raise Exception('Please inform filename')
    if not filename.__contains__('.'):
        filename = filename.strip() + '.log'

    time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    path = "resources/" + filename
    with open(cwd / path, 'a') as logfile:
        logfile.write(f'{time} [{log_type.value}] {msg} \n')


def get_last_line(filename):
    path = "resources/" + filename
    with open(cwd / path, 'r') as logfile:
        return logfile.readlines()[-1]
