import json
import codecs


with codecs.open("cookbook_json.json","r", encoding="UTF-8") as f:
    cook_book = json.load(f)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item["quantity"] *= person_count
            if new_shop_list_item["ingridient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingridient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingridient_name"]]["quantity"] += new_shop_list_item["quantity"]
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print("{ingridient_name} {quantity} {measure}".format(**shop_list_item))


def create_shop_list():
    dishes = input("введите блюда через запятую:").lower().split(",")
    person_count = int(input("Введите количество человек:"))
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()