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
