import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]
    customers = [
        Customer(
            name=c["name"],
            product_cart=c["product_cart"],
            location=c["location"],
            money=c["money"],
            car=Car(**c["car"])
        )
        for c in customers_data
    ]

    shops = [
        Shop(
            name=s["name"],
            location=s["location"],
            products_that_shop_provides=s["products"]
        )
        for s in shops_data
    ]
    # print(shops)
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            all_customers_trip = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {all_customers_trip:.2f}"
            )
            if all_customers_trip < cheapest_cost:
                cheapest_shop = shop
                cheapest_cost = all_customers_trip
        if cheapest_shop and cheapest_cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.print_receipt(customer.name, customer.product_cart)
            customer.money -= cheapest_cost
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
