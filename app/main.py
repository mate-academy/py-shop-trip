import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    shops = [
        Shop(**shop)
        for shop in data["shops"]
    ]
    customers = [
        Customer(**customer)
        for customer in data["customers"]
    ]
    fuel_price = data["FUEL_PRICE"]

    for customer in customers:
        shopping = {}
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            distance_cost = customer.distance_to_shop(shop)

            fuel_cost = customer.car.car_fuel_costs(
                fuel_price=fuel_price,
                distance=distance_cost
            ) * 2

            final_cost = round(
                (customer.product_price(shop).get(shop.name) + fuel_cost)
                , 2)

            if customer.money >= final_cost:
                shopping[final_cost] = shop

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {final_cost}")

        if not shopping:
            print(f"{customer.name} doesn't have enough money to "
                  f"make purchase in any shop")
            break

        min_shop_bill = min(key for key in shopping.keys())

        print(f"{customer.name} rides to {shopping[min_shop_bill].name}\n")

        shopping[min_shop_bill].shopping_bill(customer)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - min_shop_bill} dollars\n")


if __name__ == "__main__":
    shop_trip()
