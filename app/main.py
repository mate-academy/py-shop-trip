import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer_info in customers:
        customer = Customer(customer_info, fuel_price)
        money_str = "{:.2f}".format(round(customer.money, 2))
        print(f"{customer.name} has {money_str} dollars")

        affordable_shops = [shop for shop in shops if
                            customer.calculate_trip_cost(shop)
                            <= customer.money]

        if not affordable_shops:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        cheapest_shop = min(affordable_shops,
                            key=lambda shop:
                            customer.calculate_trip_cost(shop))
        trip_cost = customer.calculate_trip_cost(cheapest_shop)
        trip_cost_str = "{:.2f}".format(round(trip_cost, 2))
        print(f"{customer.name}'s trip to the "
              f"{cheapest_shop.name} costs {trip_cost_str} dollars")

        cheapest_shop.check_printing(customer)
        customer.money -= trip_cost
        money_str = "{:.2f}".format(round(customer.money, 2))
        print(f"{customer.name} now has {money_str} dollars")

    if __name__ == "__main__":
        shop_trip()
