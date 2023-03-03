from app.car import Car
from app.shop import Shop
from app.customer import Customer


def get_customers(customers: dict) -> list[Customer]:
    customers_list = []
    for customer in customers:
        car = Car(customer["car"]["brand"],
                  customer["car"]["fuel_consumption"])
        new_customer = Customer(customer["name"],
                                customer["product_cart"],
                                customer["location"],
                                customer["money"],
                                car)
        customers_list.append(new_customer)
    return customers_list


def get_shops(shops: dict) -> list[Shop]:
    shops_list = []
    for shop in shops:
        new_shop = Shop(shop["name"], shop["location"], shop["products"])
        shops_list.append(new_shop)
    return shops_list


def buy_products(customer: Customer,
                 chosen_shop: Shop,
                 fuel_price: float
                 ) -> None:

    print(f"{customer.name} rides to {chosen_shop.name}\n")
    print("Date: 04/01/2021 12:33:41")
    print(f"Thanks, {customer.name}, for you purchase!")
    print("You have bought: ")

    total_cost = 0
    for item, quantity in customer.product_cart.items():
        item_cost = chosen_shop.products[item] * quantity
        if isinstance(item_cost, float):
            item_cost = round(item_cost, 1)

        print(f"{quantity} {item}s for {item_cost} dollars")
        total_cost += item_cost
    print(f"Total cost is {total_cost:.1f} dollars")
    print("See you again!")
    customer.money -= customer.road_to_shop(chosen_shop, fuel_price)
    print(f"\n{customer.name} rides home")

    print(f"{customer.name} now has {customer.money:.2f} dollars\n")


def visit_shop(customer: Customer,
               shops_list: list[Shop],
               fuel_price: float
               ) -> None:

    print(f"{customer.name} has {customer.money} dollars")
    can_afford = False
    for shop in shops_list:
        trip_cost = customer.road_to_shop(shop, fuel_price)
        print(f"{customer.name}'s trip to the {shop.name}"
              f" costs {trip_cost:.2f}")
        if trip_cost <= customer.money:
            can_afford = True
    if not can_afford:
        print(f"{customer.name} doesn't have enough money "
              f"to make purchase in any shop")
        return
    chosen_shop = customer.choose_shop(shops_list, fuel_price)
    buy_products(customer, chosen_shop, fuel_price)
