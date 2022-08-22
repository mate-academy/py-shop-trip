import json
import math
import datetime


def shop_trip():
    now = datetime.datetime.now()
    date = str(now.date()).split("-")
    date = date[2] + "/" + date[1] + "/" + date[0]
    time = str(now.time()).split(".")
    time = time[0]
    with open("config.json", "r") as info:
        information = json.load(info)
    FUEL_PRICE = information['FUEL_PRICE']
    customers = information["customers"]
    shops = information["shops"]
    for customer in range(len(customers)):
        name = customers[customer]["name"]
        amount_money = customers[customer]["money"]
        print(f"{name} has {amount_money} dollars")
        fuel_consumption = customers[customer]["car"]["fuel_consumption"]
        location_cust = customers[customer]["location"]
        amount_milk = customers[customer]["product_cart"]["milk"]
        amount_bread = customers[customer]["product_cart"]["bread"]
        amount_butter = customers[customer]["product_cart"]["butter"]
        one_km_cost = FUEL_PRICE * fuel_consumption / 100
        shops_dict_cost = {}
        shops_dict_distance = {}
        for shop in range(len(shops)):
            index_shops = shops.index(shops[shop])
            shop_name = shops[shop]["name"]
            location_shop = shops[shop]["location"]
            distance_to_shop = math.sqrt(
                (location_shop[0] - location_cust[0]) ** 2 +
                (location_shop[1] - location_cust[1]) ** 2)
            distance_to_shop_cost = round(one_km_cost * distance_to_shop * 2, 2)
            shops_dict_distance[index_shops] = distance_to_shop_cost
            milk_cost = shops[shop]["products"]["milk"] * amount_milk
            bread_cost = shops[shop]["products"]["bread"] * amount_bread
            butter_cost = shops[shop]["products"]["butter"] * amount_butter
            total_cost = milk_cost + bread_cost + butter_cost
            trip_to_shop_cost = distance_to_shop_cost + total_cost
            shops_dict_cost[index_shops] = trip_to_shop_cost
            print(f"{name}'s trip to the {shop_name} costs {trip_to_shop_cost}")
        optimal_shop_index = min(shops_dict_cost, key=shops_dict_cost.get)
        optimal_shop_name = shops[optimal_shop_index]["name"]
        optimal_shop_cost = shops_dict_cost[optimal_shop_index]
        optimal_shop_dist = shops_dict_distance[optimal_shop_index]
        if customers[customer]["money"] < optimal_shop_cost:
            print(f"{name} doesn't have enough money to make purchase in any shop")
        else:
            print(f"{name} rides to {optimal_shop_name}" + "\n")
            print(f"Date: {date} {time}")
            print(f"Thanks, {name}, for you purchase!")
            print("You have bought: ")
            for shop_ in shops:
                if shop_["name"] == optimal_shop_name:
                    milk_cost_optimal = shop_["products"]["milk"] * amount_milk
                    bread_cost_optimal = shop_["products"]["bread"] * amount_bread
                    butter_cost_optimal = shop_["products"]["butter"] * amount_butter
                    total_cost_optimal = milk_cost_optimal + bread_cost_optimal + butter_cost_optimal
                    rest_of_money = customers[customer]["money"] - total_cost_optimal - optimal_shop_dist
                    print(f"{amount_milk} milks for {milk_cost_optimal} dollars")
                    print(f"{amount_bread} breads for {bread_cost_optimal} dollars")
                    print(f"{amount_butter} butters for {butter_cost_optimal} dollars")
                    print(f"Total cost is {total_cost_optimal} dollars")
                    print("See you again!" + "\n")
                    print(f"{name} rides home")
                    print(f"{name} now has {rest_of_money} dollars" + "\n")






print(shop_trip())

# Bob has 55 dollars
# Bob's trip to the Outskirts Shop costs 28.21
# Bob's trip to the Shop '24/7' costs 31.48
# Bob rides to Outskirts Shop
#
# Date: 2021/01/04 12:33:41
# Thanks, Bob, for you purchase!
# You have bought:
# 4 milks for 12 dollars
# 2 breads for 2 dollars
# 5 butters for 12.5 dollars
# Total cost is 26.5 dollars
# See you again!
#
# Bob rides home
# Bob now has 26.79 dollars
#
# Monica has 12 dollars
# Monica's trip to the Outskirts Shop costs 15.65
# Monica's trip to the Shop '24/7' costs 16.84
# Monica doesn't have enough money to make purchase in any shop


# Вы хотите создать приложение, которое помогает клиентам выбирать самую дешевую поездку для продуктов.
#
# Есть config.json файл, который содержит:
# FUEL_PRICE- Цена за 1 литр топлива в долларах.
# customers- список словарей с информацией о каждом клиенте.
# shops- список словарей с информацией о каждом магазине в городе.
# У вас есть информация о:
# Customers: имя, продукты которые он хочет купить, расположение, Деньги, автомобиль, марка,объем расхода топлива на 100 км.
# Shops: имя, расположение, продукты, которые предлагает магазин

# Напишите shop_trip функцию, не принимающую никаких аргументов, в которой покупатели вычисляют,
# сколько будет стоить поездка за продуктами в каждом магазине, выбирают самый дешевый и едут туда,
# если у них достаточно денег. Когда покупатель приходит в магазин,
# его местоположение должно совпадать с местоположением магазина.
# После того, как покупатель покупает товары, магазин распечатывает чек о покупке,
# используя текущее время. После магазина он приходит домой и считает оставшиеся деньги.
#
# Стоимость поездки состоит из трех частей: стоимость топлива до магазина,
# стоимость всех продуктов для покупки, стоимость топлива до дома.
# Вы сами разрабатываете архитектуру приложения.
#
# Расстояние между покупателем и магазином — это расстояние между их местоположениями в км.
# Округлите напечатанное значение до двух знаков после запятой.