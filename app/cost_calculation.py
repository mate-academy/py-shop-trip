import json
import operator

from app.customer import Customer
from app.shop import Shop


def calc_distance_cost(
        person: Customer,
        shop: Shop
) -> float:
    return (
        (person.location[0] - shop.location[0]) ** 2
        + (person.location[1] - shop.location[1]) ** 2
    )**0.5


def calc_location_cost(
        distance: float,
        fuel_price: float,
        person: Customer
) -> int:
    return (distance / 100) * fuel_price * person.car["fuel_consumption"]


def calculate_all_prices(
        customers: list,
        shops: list,
        fuel_price: float
) -> list:
    all_customer_price = []
    for person in customers:
        each_customer_price = {}
        for shop_ in shops:
            distance = calc_distance_cost(person, shop_)
            location_cost = calc_location_cost(distance, fuel_price, person)
            product_cost = sum(list(map(operator.mul,
                                        person.product_cart.values(),
                                        shop_.products.values())))
            each_customer_price.update(
                {shop_.name: round(location_cost * 2 + product_cost, 2)}
            )
        all_customer_price.append(each_customer_price)
    return all_customer_price


def give_output() -> None:
    with open("app/config.json", "r") as j_file:
        info = json.load(j_file)

    fuel_price = info["FUEL_PRICE"]

    customers = [Customer(**customer) for customer in info["customers"]]
    shops = [Shop(**shop) for shop in info["shops"]]

    all_customer_price = calculate_all_prices(customers, shops, fuel_price)

    for person, trip in enumerate(all_customer_price):
        name = customers[person].name
        f_shop, s_shop, t_shop = trip.values()
        print(f"{name} has {customers[person].money} dollars\n"
              f"{name}'s trip to the Outskirts Shop costs {f_shop}\n"
              f"{name}'s trip to the Shop '24/7' costs {s_shop}\n"
              f"{name}'s trip to the Central Shop costs {t_shop}")
        min_exp = min(trip.values())
        min_ind = list(trip.values()).index(min_exp)
        if min_exp > customers[person].money:
            print(f"{name} doesn't have enough money"
                  f" to make a purchase in any shop")
        else:
            shop_name = shops[min_ind].name
            print(f"{name} rides to {shop_name}\n"
                  "\nDate: 04/01/2021 12:33:41\n"
                  f"Thanks, {name}, for your purchase!\n"
                  "You have bought:")
            product_keys = ["milk", "bread", "butter"]
            cost = 0
            for product_key in product_keys:
                quantity = customers[person].product_cart[product_key]
                shop_price = shops[min_ind].products[product_key]
                product_cost = quantity * shop_price
                cost += product_cost
                if str(product_cost)[-1] == "0":
                    product_cost = round(product_cost)
                print(f"{quantity} {product_key}s for {product_cost} dollars")
            remain = (customers[person].money
                      - all_customer_price[person][shop_name])
            print(f"Total cost is {cost} dollars\n"
                  "See you again!\n"
                  f"\n{name} rides home\n"
                  f"{name} now has {remain} dollars\n")
