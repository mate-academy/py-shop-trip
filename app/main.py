import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as json_file:
        data = json.load(json_file)
    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**entry) for entry in data["customers"]]
    shops = [Shop(**entry) for entry in data["shops"]]
    all_text = []
    for customer in customers:
        money = f"{customer.money:.2f}"
        to_print = [f"{customer.name} has {money} dollars"]
        all_trips = []
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            to_print.append(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost:.2f}"
            )
            all_trips.append((trip_cost, shop))
        cost, shop = min(all_trips, key=lambda item: item[0])
        if cost > customer.money:
            to_print.append(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            all_text.append("\n".join(to_print))
            continue
        to_print.append(f"{customer.name} rides to {shop.name}\n")
        products_expenses = customer.get_products_expense(shop)
        to_print.append(
            shop.get_check(
                customer.name,
                customer.product_cart,
                products_expenses
            )
        )
        to_print.append(f"\n{customer.name} rides home")
        customer.spend_money(cost)
        money = f"{customer.money:.2f}"
        to_print.append(f"{customer.name} now has {money} dollars")
        all_text.append("\n".join(to_print))
    print("\n\n".join(all_text))
