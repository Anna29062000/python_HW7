from view import action
from model import model_record, model_print, data_collector

def begin_prog():
    while (True):
        value = action()
        if value == 0:
            break
        elif value == 1:
            model_print()
        elif value == 2:
            data = data_collector()
            model_record(data)
