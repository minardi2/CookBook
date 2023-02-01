from pprint import pprint

def get_recipes(recipes_file='recipes_ru.txt'):
    cook_book = {}
    with open(recipes_file, 'rt', encoding='utf-8') as receipt_file:
        while True:
            dish = receipt_file.readline().rstrip('\n').lower()
            if not dish:
                break
            cook_book[dish] = []
            n = int(receipt_file.readline().rstrip('\n'))
            items = [receipt_file.readline().rstrip('\n').rsplit('|') for _ in range(n)]
            for item in items:
                cook_book[dish].append({'ingredient_name': item[0].rstrip(),
                                        'quantity': int(item[1].replace(' ', '')),
                                        'measure': item[2].replace(' ', '')})
            receipt_file.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете '
                   'на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)

cook_book = get_recipes()
create_shop_list(cook_book)
pprint(get_recipes())
