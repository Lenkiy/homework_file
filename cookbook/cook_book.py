def read_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredients_number = int(f.readline().strip())
            ingredients_list = []
            for i in range(ingredients_number):
                ingredient_line = f.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingredients_list
            f.readline()
    return cook_book

cook_book = read_cook_book('recipes.txt')
# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient_name] = {'quantity': ingredient['quantity'] * person_count, 'measure': ingredient['measure']}
    return shop_list


cook_book = read_cook_book('recipes.txt')
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list)
