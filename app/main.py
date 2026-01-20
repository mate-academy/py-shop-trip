import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as json_file:
        data = json.load(json_file)

    fuel_price = data["FUEL_PRICE"]
    customer_data = data["customers"]
    shop_data = data["shops"]

    customers = []
    shops = []

    for cust in customer_data:
        car = Car(
            brand=cust["car"]["brand"],
            fuel_consumption=cust["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=cust["name"],
            product_cart=cust["product_cart"],
            location=cust["location"],
            money=cust["money"],
            car=car
        )
        customers.append(customer)

    for shop in shop_data:
        shop_obj = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        shops.append(shop_obj)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = []
        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            costs.append((shop, cost))
            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost:.2f}"
            )

        costs.sort(key=lambda x: x[1])
        cheapest_shop, cheapest_cost = costs[0]

        if customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            print()  # Порожній рядок перед чек
            cheapest_shop.print_receipt(customer)
            print()  # Порожній рядок після чеку
            print(f"{customer.name} rides home")
            customer.money -= cheapest_cost
            print(f"{customer.name} now has {customer.money:.2f} dollars")
            print()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
