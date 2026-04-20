import json
from app.customer import Customer
from app.models import Car, Shop
from app.utils import distance  # Функція вже в utils.py


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**s_data) for s_data in config["shops"]]

    for c_data in config["customers"]:
        home_location = c_data["location"]

        customer = Customer(
            name=c_data["name"],
            location=home_location,
            car=Car(c_data["car"]["brand"], c_data["car"]["fuel_consumption"]),
            money=c_data["money"],
            cart=c_data["product_cart"]
        )

        # Тест хоче "55 dollars", а не "55.00", тому :g
        print(f"{customer.name} has {customer.money:g} dollars")

        cheapest_shop = None
        min_total_cost = float("inf")
        best_products_cost = 0

        for shop in shops:
            dist = distance(home_location, shop.location)
            fuel_cost = customer.car.get_trip_cost(dist * 2, fuel_price)
            p_cost = shop.get_products_cost(customer.cart)

            # Округляємо до 2 знаків для логіки
            total_trip_cost = round(fuel_cost + p_cost, 2)

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_trip_cost:g}")

            if total_trip_cost < min_total_cost:
                min_total_cost = total_trip_cost
                cheapest_shop = shop
                best_products_cost = p_cost

        if cheapest_shop and customer.money >= min_total_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")

            customer.location = cheapest_shop.location
            customer.money -= min_total_cost

            customer.print_receipt(cheapest_shop, best_products_cost)

            print(f"\n{customer.name} rides home")
            customer.location = home_location
            # Для "Bob now has 26.79" формат :g теж спрацює ідеально
            print(f"{customer.name} now has {round(customer.money, 2):g} "
                  f"dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make "
                  f"a purchase in any shop")
