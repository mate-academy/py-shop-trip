from json import load
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as data:
        data_file = load(data)

    shops = []
    customers = []
    fuel_price = data_file.get("FUEL_PRICE")

    for shop in data_file.get("shops"):
        shops.append(
            Shop(
                shop.get("name"),
                shop.get("location"),
                shop.get("products")
            )
        )

    for customer in data_file.get("customers"):
        customers.append(
            Customer(
                customer.get("name"),
                customer.get("product_cart"),
                customer.get("location"),
                customer.get("money"),
                Car(
                    customer.get("car")["brand"],
                    customer.get("car")["fuel_consumption"]
                )
            )
        )

    for customer in customers:
        print(customer.count_money())

        for key, value in customer.total_cost(shops, fuel_price).items():
            print(f"{customer.name}'s trip to the {key} costs {value}")
        min_trip = customer.min_total_cost(shops, fuel_price)

        if customer.total_cost(shops, fuel_price)[min_trip] < customer.money:
            print(f"{customer.name} rides to {min_trip}")
            print()

            for shop in shops:
                if shop.name == min_trip:
                    shop.get_check(customer)
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money_remains(shops, fuel_price, min_trip)} "
                  f"dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make "
                  f"purchase in any shop")
