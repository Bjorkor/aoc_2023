import pandas as pd
import re
from icecream import ic

def words_2_int(row):
    new_row = None
    sub_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for item in sub_dict:
        if new_row is None:
            new_row = re.sub(item, sub_dict[item], row)
        else:
            new_row = re.sub(item, sub_dict[item], new_row)
    ic(new_row)
    return new_row
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
words_series = content_series.apply(words_2_int)
answer_series = words_series.apply(get_cb_value)
final_cb = answer_series.sum() 
print(final_cb)

