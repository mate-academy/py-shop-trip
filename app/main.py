import json


def shop_trip():
    my_dic = {}
    with open('app/config.json')as file:
        data = json.load(file)
        my_dic.update(data)

    fuel_price = my_dic["FUEL_PRICE"]
    shops = []
    customers = []
    customers += (my_dic["customers"])
    shops += (my_dic["shops"])
    shop_list_each_name_each_store = []
    for name in range(len(customers)):
        sum_for_name_for_each_store = []
        for shop in range(len(shops)):
            price = 0
            price += customers[name]["product_cart"]['milk'] * \
                shops[shop]["products"]['milk']
            price += customers[name]["product_cart"]['bread'] * \
                shops[shop]["products"]['bread']
            price += customers[name]["product_cart"]['butter'] * \
                shops[shop]["products"]['butter']
            my = customers[name]["location"]
            mall = shops[shop]["location"]
            dist = ((my[0] - mall[0]) ** 2 + (my[1] - mall[1]) ** 2) ** 0.5
            car_eats = customers[name]["car"]["fuel_consumption"]
            fuel = fuel_price * dist * car_eats * 2 / 100
            price += fuel
            sum_for_name_for_each_store.append(round(price, 2))
        shop_list_each_name_each_store.append(sum_for_name_for_each_store)

    for person in range(len(customers)):
        budget = customers[person]["money"]
        food = customers[person]['product_cart']
        print(f"{customers[person]['name']} "
              f"has {customers[person]['money']} dollars")
        print(f"{customers[person]['name']}'s trip to the Outskirts Shop "
              f"costs {shop_list_each_name_each_store[person][0]}")
        print(f"{customers[person]['name']}'s trip to the Shop \'24/7\' "
              f"costs {shop_list_each_name_each_store[person][1]}")
        print(f"{customers[person]['name']}'s trip to the Central Shop "
              f"costs {shop_list_each_name_each_store[person][2]}")
        if budget < \
                min(shop_list_each_name_each_store[person]):
            print(f"{customers[person]['name']} doesn\'t "
                  f"have enough money to make purchase in any shop")
        else:
            if min(shop_list_each_name_each_store[person]) == \
                    shop_list_each_name_each_store[person][0]:
                shop_id = 0
                print(f"{customers[person]['name']} rides to Outskirts Shop")
            elif min(shop_list_each_name_each_store[person]) == \
                    shop_list_each_name_each_store[person][1]:
                shop_id = 1
                print(f"{customers[person]['name']} rides to Shop \'24/7\'")
            elif min(shop_list_each_name_each_store[person]) == \
                    shop_list_each_name_each_store[person][2]:
                shop_id = 2
                print(f"{customers[person]['name']} rides to Central Shop")
            print("")
            print("Date: 11/03/2020 13:15:34")
            milk_price = customers[person]["product_cart"]["milk"] * \
                shops[shop_id]["products"]["milk"]
            bread_price = customers[person]["product_cart"]["bread"] * \
                shops[shop_id]["products"]["bread"]
            butter_price = customers[person]["product_cart"]["butter"] * \
                shops[shop_id]["products"]["butter"]
            total_cost = milk_price + bread_price + butter_price
            market = shops[shop_id]["location"]
            home = customers[person]["location"]
            x_coord_square = (home[0] - market[0]) ** 2
            y_coord_square = (home[1] - market[1]) ** 2
            distance = (x_coord_square + y_coord_square) ** 0.5
            car_drinks = customers[person]["car"]["fuel_consumption"]
            fuel_cost = fuel_price * distance * car_drinks * 2 / 100
            money_left = round(budget - total_cost - fuel_cost, 2)
            print(f"Thanks, {customers[person]['name']}, for you purchase!")
            print(f"You have bought: \n"
                  f"{food['milk']} milks for {milk_price} dollars\n"
                  f"{food['bread']} breads for {bread_price} dollars\n"
                  f"{food['butter']} butters for {butter_price} dollars")
            print(f"Total cost is {total_cost} dollars")
            print("See you again!")
            print("")
            print(f"{customers[person]['name']} rides home")
            print(f"{customers[person]['name']} now has {money_left} dollars")
            print("")
