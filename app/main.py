import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    shops = [Shop(shop) for shop in data["shops"]]
    customers = [Customer(customer) for customer in data["customers"]]
    for customer in customers:
        go_shopping = {}
        car = Car(customer.car)
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            distance_cost = customer.calculate_distance_to_shop(shop)
            fuel_cost = car.car_fuel_costs(
                data["FUEL_PRICE"], distance_cost) * 2
            final_cost = round((customer.product_price(shop).get(shop.name)
                                + fuel_cost), 2)
            if customer.money >= final_cost:
                go_shopping[final_cost] = shop
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {final_cost}")
        if not go_shopping:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
            break
        min_shop_bill = min(key for key in go_shopping.keys())
        print(f"{customer.name} rides to {go_shopping[min_shop_bill].name}\n")
        go_shopping[min_shop_bill].shopping_bill(customer)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now "
              f"has {customer.money - min_shop_bill} dollars\n")


if __name__ == "__main__":
    shop_trip()
