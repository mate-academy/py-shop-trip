import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(customer, fuel_price)
                 for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_trip_cost = 0

        for shop in shops:
            cost = customer.calculate_trip_cost(shop)

            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            if not cheapest_shop or cost < cheapest_trip_cost:
                cheapest_shop = shop
                cheapest_trip_cost = cost

        if customer.money < cheapest_trip_cost:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.check_printing(customer)

        print(f"{customer.name} rides home")
        customer.location = customer.home_location

        customer.money -= cheapest_trip_cost
        print(f"{customer.name} now has {customer.money} dollars\n")


if __name__ == "__main__":
    shop_trip()
