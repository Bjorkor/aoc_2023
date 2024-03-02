import pandas as pd
from icecream import ic


def get_cb_value(row):
    char_list = []
    for char in row:
        if char.isdigit():  
            char_list.append(char)
    if len(char_list) == 1:
        calibration_value = int(char_list[0] * 2) 
    elif len(char_list) == 2:
        calibration_value = int(char_list[0] + char_list[1])
    elif len(char_list) > 2:
        calibration_value = int(char_list[0] + char_list[-1])
    else:
        return None
    return calibration_value 
with open('day1input.txt') as file:
    content = file.read()

split_content = content.split('\n')
content_series = pd.Series(split_content)
answer_series = content_series.apply(get_cb_value)
final_cb = answer_series.sum() 
print(final_cb)
