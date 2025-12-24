import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

        fuel_price = config["FUEL_PRICE"]

        shops = [Shop(**shop) for shop in config["shops"]]
        customers = [
            Customer(
                name=c["name"],
                product_cart=c["product_cart"],
                location=c["location"],
                money=c["money"],
                car=Car(**c["car"])
            )
            for c in config["customers"]
        ]

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            trip_costs = []

            # Зберігаємо витрати на кожен магазин та виводимо
            for shop in shops:
                cost = customer.trip_cost(shop, fuel_price)
                trip_costs.append((shop, cost))
                print(f"{customer.name}'s "
                      f"trip to the {shop.name} costs {cost}")

            # Знаходимо найдешевший магазин
            cheapest_shop, cheapest_cost = min(trip_costs, key=lambda x: x[1])

            if customer.money >= cheapest_cost:
                # Зберігаємо домашню локацію перед поїздкою
                home_location = customer.location.copy()

                # Поїздка в магазин
                print(f"{customer.name} rides to {cheapest_shop.name}\n")
                customer.location = cheapest_shop.location.copy()

                # Чек
                cheapest_shop.print_receipt(
                    customer.name,
                    customer.product_cart)

                # Повернення додому
                print(f"{customer.name} rides home")
                customer.location = home_location

                # Оновлення грошей
                customer.money -= cheapest_cost
                customer.money = round(customer.money, 2)
                print(f"{customer.name} now has {customer.money} dollars")
                print()
            else:
                print(f"{customer.name} doesn't have"
                      f" enough money to make a purchase in any shop")
