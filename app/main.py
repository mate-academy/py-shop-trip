import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        fuel_price, customers, shops = data.values()
        people = [Customer(*customer.values()) for customer in customers]
        citi_shops = [Shop(*shop.values()) for shop in shops]

        for person in people:
            print(f"{person.name} has {person.money} dollars")
            total_costs = []
            for shop in citi_shops:
                total_costs.append(
                    (shop, person.calculate_trip_expenses(
                        shop, fuel_price)
                     )
                )
                print(f"{person.name}'s trip to the {total_costs[-1][0].name}"
                      f" costs {total_costs[-1][1]}")
            cheapest_shop, spending = min(total_costs, key=lambda x: x[1])

            if person.money < spending:
                print(f"{person.name} doesn't have enough money"
                      f" to make a purchase in any shop")
                continue

            print(f"{person.name} rides to {cheapest_shop.name}")
            person.shopping(cheapest_shop)
            person.money = person.money - spending

            print(f"{person.name} rides home")
            print(f"{person.name} now has {person.money} dollars")
            print()


if __name__ == "__main__":
    shop_trip()
