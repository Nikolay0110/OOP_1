from pprint import pprint


def read_cookbook():
    cook_book = {}
    with open('recipes.txt', encoding='UTF-8') as file:
        for line in file:
            name = line.strip()
            emp_count = int(file.readline())
            dish = []
            for i in range(emp_count):
                x = file.readline().strip()
                ingredient, quantity, tipe = x.split(' | ')
                dish.append(
                    {'ingredient': ingredient,
                     'quantity': int(quantity),
                     'type': tipe
                     })
            cook_book[name] = dish
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cookbook()
    shop_list = {}
    for dish in dishes:
        for el in cook_book[dish]:
            if el['ingredient'] not in shop_list:
                shop_list[el['ingredient']] = {'type': el['type'],
                                               'quantity': el['quantity'] * person_count}
            else:
                shop_list[el['ingredient']]['quantity'] += el['quantity'] * person_count
    return pprint(shop_list)


print('___Задание 1___')
print()
pprint(read_cookbook(), width=100)
print()
print('___Задание 2___')
print()
get_shop_list_by_dishes(
    ['Запеченный картофель', 'Омлет', 'Фахитос', 'Утка по-пекински'], 5)
print()
print('___Задание 3___')
print()


# def read_files(txt_list):
#     txt_dict = {}
#     for book in txt_list:
#         with open(book, encoding='UTF-8') as file:
#             counter = 0
#             for line in file:
#                 counter += 1
#             txt_dict[book] = counter
#     ready_dict = sorted(txt_dict.items(), key=lambda item: item[1])
#     return print(ready_dict)
#
#
# read_files(['1.txt', '2.txt', '3.txt'])


# def open_dict(name):
#     with open("result.txt", "w", encoding="UTF-8") as d:
#         basic_dict = {}
#         for i in name:
#             with open(i, encoding="UTF-8") as f: a = f.readlines()
#             basic_dict[i] = len(a)
#         for keys, values in sorted(basic_dict.items(), key=lambda item: item[1]):
#             d.writelines(f'{keys}\n{str(values)}\n')
#             for line in open(keys, encoding="UTF-8"): d.writelines(line)
#
#
# list_1 = ["1.txt", "2.txt", "3.txt"]
# open_dict(list_1)


def read_files(txt_list):  # Читаем файлики и записываем их по кол-ву строк в новый файл, ю ноу...
    txt_dict = {}
    ready_txt = open('final_text.txt', 'w', encoding='UTF-8')
    for book in txt_list:
        with open(book, encoding='UTF-8') as file:
            counter = 0
            for line in file:
                counter += 1
            txt_dict[book] = counter
    for key, value in sorted(txt_dict.items(), key=lambda p: p[1]):
        ready_txt.writelines(f'{key}\n{value}\n')
        for line in open(key, encoding='UTF-8'):
            ready_txt.writelines(line)
        ready_txt.writelines('\n')
    ready_txt.close()
    print(txt_dict)


read_files(['1.txt', '2.txt', '3.txt'])