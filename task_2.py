def get_count_char(str_):
    dict_ = {}
    new_str = str_.lower()
    for symbol in new_str:
        if symbol.isalpha():
            if symbol in dict_:
                dict_[symbol] += 1
            else:
                dict_[symbol] = 1
    return dict_

def percent_char(dict_):
    percent_dict = {}
    for key in dict_:
        percent_dict[key] = round((dict_[key]* 100 / sum(dict_.values()), 2))
    return percent_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
