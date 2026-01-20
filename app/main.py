import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file_open:
        data = json.load(file_open)

    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        car = Car(customer.car)

        print(f"{customer.name} has {customer.money} dollars")

        shops_to_go = {}
        for shop in shops:
            distance = customer.calculate_distance(shop)
            cost = car.travel_costs(distance, data["FUEL_PRICE"])
            total_cost = round((shop.calculate_products_price(
                customer.product_cart) + cost), 2)

            if total_cost <= customer.money:
                shops_to_go[total_cost] = shop

            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost}")

        if not shops_to_go:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
            break

        minimal_cost = min(key for key in shops_to_go.keys())

        print(f"{customer.name} rides to "
              f"{shops_to_go[minimal_cost].name}\n")

        shops_to_go[minimal_cost].receipt(customer.name,
                                          customer.product_cart)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now "
              f"has {customer.money - minimal_cost} dollars\n")


if __name__ == "__main__":
    shop_trip()
