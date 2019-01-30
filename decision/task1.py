FILENAME = 'for_test.log'

def read_log(filename):
    keyword = 'eid:'
    with open(filename, "r") as file:
        lines = file.readlines()
        result_list = []
        # Перебор файла с конца
        for row_sting in lines[::-1]:
            index = row_sting.find(keyword)
            if index >= 0:
                # Отнимаем искомое слово от результата поиска
                sub_log = row_sting[index + len(keyword):]
                # Создаем словарь, разбиваем и записываем в него результаты
                result_dict = {}
                for key_value in sub_log.split(';'):
                    key, value = key_value.split('.')
                    result_dict[key] = value
                result_list.append(result_dict.copy())
            # Когда нашли 2 последних, сравниваем их
            if len(result_list) >= 2:
                dict_last, dict_no_last = result_list
                compere_dict = {}
                for key, value in dict_last.items():
                    if key not in dict_no_last or dict_no_last[key] != dict_last[key]:
                        if key not in compere_dict:
                            compere_dict[key] = {}
                        compere_dict[key]['last'] = value
                for key, value in dict_no_last.items():
                    if key not in dict_last or dict_no_last[key] != dict_last[key]:
                        if key not in compere_dict:
                            compere_dict[key] = {}
                        compere_dict[key]['no_last'] = value

                # Вывод значений
                print(f'Последний {dict_last}')
                print(f'Проедпоследний {dict_no_last}')
                print(f'Различия {compere_dict}')
                break

if __name__ == '__main__':
    read_log(FILENAME)