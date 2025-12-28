import math


def get_info(customer: dict, data):
    consumption = customer["car"]["fuel_consumption"]
    cart = customer["product_cart"]
    result_dict = {"name": customer["name"],
                   "result_strings": [],
                   "shop_and_price": {},
                   "has_enough_money": []}

    for shop in data["shops"]:

        distance = math.dist(customer["location"], shop["location"]) * 2
        fuel_price = distance * data["FUEL_PRICE"] * consumption / 100
        products_price = sum(shop["products"][item] * cart[item]
                             for item in cart)
        price_to_shop = round(fuel_price + products_price, 2)

        string = f"{customer['name']}'s trip to the " \
                 f"{shop['name']} costs {price_to_shop}"

        result_dict["result_strings"].append(string)
        result_dict["shop_and_price"][shop["name"]] = price_to_shop
        result_dict["has_enough_money"].append(
            customer["money"] > price_to_shop
        )

    if not any(result_dict["has_enough_money"]):
        result_dict["has_enough_money"] = False
        return result_dict

    else:
        result_dict["has_enough_money"] = True
        result_dict["cheapest"] = min(result_dict["shop_and_price"],
                                      key=result_dict["shop_and_price"].get)
        string = f"{customer['name']} rides to {result_dict['cheapest']}\n"
        result_dict["result_strings"].append(string)

    return result_dict


def choose_the_cheapest_shop(customer, customer_info, data):
    result = {}
    cart = customer["product_cart"]
    shops = data["shops"]
    shop_by_price = customer_info["shop_and_price"]

    for shop in shops:
        if customer_info["has_enough_money"] and \
                shop["name"] == customer_info["cheapest"]:

            result["items"] = {item: cart[item] * shop["products"][item]
                               for item, price in shop["products"].items()}
            result["total_cost"] = sum(result["items"].values())
            result["money_left"] = round(
                customer["money"] - min(shop_by_price.values()), 2
            )

    return result


def print_info(customer_info):

    for string in customer_info["result_strings"]:
        print(string)

    if not customer_info["has_enough_money"]:
        print(f"{customer_info['name']} doesn't have enough money "
              f"to make purchase in any shop")
