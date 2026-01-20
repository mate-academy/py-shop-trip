import datetime
from app.claasss import Customer, Shops
from app.fiilee import Config


def shop_trip() -> None:
    config = Config("app/config.json")
    res_shop = []
    for elem in config.shops:
        res_shop.append(Shops(elem["name"],
                              elem["location"],
                              elem["products"]))

    res_customer = []
    for elem in config.customers:
        res_customer.append(Customer(elem["name"],
                                     elem["product_cart"],
                                     elem["location"],
                                     elem["money"],
                                     elem["car"]))

    price_for_fuel = config.fuel_price
    for elem in res_customer:

        print(f"{elem.name} has {elem.money} dollars")
        res = {}
        for shop in res_shop:
            distance = ((elem.location[0] - shop.location[0]) ** 2
                        + (elem.location[1] - shop.location[1]) ** 2) ** 0.5
            liters_needed = (distance / 100) * elem.car["fuel_consumption"]
            price = liters_needed * price_for_fuel
            money_need = ((elem.product_cart["milk"]
                           * shop.products["milk"]
                           + elem.product_cart["bread"]
                           * shop.products["bread"]
                           + elem.product_cart["butter"]
                           * shop.products["butter"])
                          + price * 2)
            res[shop.name] = money_need
            print(f"{elem.name}'s trip to the "
                  f"{shop.name} costs {round(money_need, 2)}")
        min_key = min(res, key=res.get)
        min_value = res[min_key]
        if elem.money > min_value:
            print(f"{elem.name} rides to {min_key}")
            elem.money -= min_value
        else:
            print(f"{elem.name} doesn't have "
                  f"enough money to make a purchase in any shop")

        count_point = 0
        list_product_count = []
        list_price = []
        list_product = []
        for el in elem.product_cart:
            list_product.append(el)
            list_product_count.append(elem.product_cart[el])
            for cost in res_shop:
                if cost.name == min_key:
                    count_val = cost.products[el]
                    list_price.append(count_val)
            count_point += elem.product_cart[el] * count_val

        if elem.money >= count_point:
            print(f"\nDate: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                  f"Thanks, {elem.name}, for your purchase!\n"
                  f"You have bought:")
            total_cost = 0
            for i in range(len(list_product)):
                prices = list_product_count[i] * list_price[i]
                str_prices = str(prices)
                mn = "s"
                if str_prices[-1] == "0":
                    print(f"{list_product_count[i]} "
                          f"{list_product[i] + mn} for "
                          f"{int(prices)} dollars")
                else:
                    print(f"{list_product_count[i]} "
                          f"{list_product[i] + mn} for "
                          f"{prices} dollars")
                total_cost += list_product_count[i] * list_price[i]
            print(f"Total cost is {total_cost} dollars\n"
                  f"See you again!\n")
            print(f"{elem.name} rides home\n"
                  f"{elem.name} now has {round(elem.money, 2)} dollars\n")
