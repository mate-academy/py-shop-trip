import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)
    costs = {}
    fuel_price = data.get("FUEL_PRICE")
    customers = [Customer(**customer) for customer in data.get("customers")]
    shops = [Shop(**shop) for shop in data.get("shops")]
    for customer in customers:
        home_location = customer.location
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            distance = customer.get_distance(customer.location, shop.location)
            fuel_cost = customer.calculate_fuel_cost(
                distance, fuel_price, customer.car.fuel_consuption
            )
            product_cost = customer.get_product_price(
                customer.product_cart, shop.products
            )
            costs[round(fuel_cost + product_cost, 2)] = shop
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(fuel_cost + product_cost, 2)}"
            )
        cheapest_shop = min(costs)
        if customer.money > cheapest_shop:
            print(f"{customer.name} rides to {costs[cheapest_shop].name}\n")
            customer.location = costs[cheapest_shop].location
            customer.print_purchase_receipt(
                customer.name,
                customer.product_cart,
                costs[cheapest_shop].products
            )
            print(f"{customer.name} rides home")
            customer.location = home_location
            total = customer.count_money(customer.money, cheapest_shop)
            print(f"{customer.name} now has {total} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
