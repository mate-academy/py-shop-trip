import json
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> str:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    shops_list = []
    customers_list = []

    for shop_data in data["shops"]:
        new_shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops_list.append(new_shop)
    for customer_data in data["customers"]:
        new_customer = Customer(customer_data, fuel_price)
        customers_list.append(new_customer)

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        min_cost = float("inf")

        for shop in shops_list:
            cost = customer.calculate_trip_cost(shop)
            cost = round(cost, 2)
            print(f"{customer.name}'s "
                  f"trip to the {shop.name} costs {cost}")
            if cost < min_cost:
                min_cost = cost
                cheapest_shop = shop
        if customer.money >= min_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            cheapest_shop.print_receipt(customer.name, customer.product_cart)
            customer.money -= min_cost
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money "
                  f"to make a purchase in any shop")
