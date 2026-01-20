import json

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data.get("FUEL_PRICE")

    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]
    customer_cars = {
        customer["name"]:
            Car(**customer["car"]) for customer in data["customers"]
    }

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        dict_shops_costs = {}
        for shop in shops:
            car = customer_cars[customer.name]
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {customer.total_costs(car, shop, fuel_price)}")
            dict_shops_costs.update(
                {
                    shop.name: customer.total_costs(car, shop, fuel_price)
                }
            )

        min_cost_shop = min(
            shops,
            key=lambda shop: customer.total_costs(car, shop, fuel_price),
            default=None
        )
        if min_cost_shop:
            cost_to_shop = customer.total_costs(car, min_cost_shop, fuel_price)
            if cost_to_shop < customer.money:
                print(f"{customer.name} rides to {min_cost_shop.name}\n")
                min_cost_shop.print_check(customer)
                print(f"\n{customer.name} rides home")
                customer.money -= cost_to_shop
                print(f"{customer.name} now has {customer.money} dollars\n")
            else:
                print(f"{customer.name} doesn't have enough money"
                      f" to make a purchase in any shop")
        else:
            print("No shops available")
