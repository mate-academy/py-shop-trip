from datetime import datetime
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    import json

    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer(
            name=data["name"],
            product_cart=data["product_cart"],
            location=data["location"],
            money=data["money"],
            car_data=data["car"]
        )
        for data in config["customers"]
    ]
    shops = [
        Shop(
            name=data["name"],
            location=data["location"],
            products=data["products"]
        )
        for data in config["shops"]
    ]

    for customer in customers:
        print(f"\n{customer.name} has ${customer.money}")
        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to {shop.name} costs {cost}")
            if cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_shop = shop

        if cheapest_cost <= customer.money:
            customer.location = cheapest_shop.location

            print(f"{customer.name} rides to {cheapest_shop.name}")
            print(f"\nDate: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            total_cost = 0
            for product, amount in customer.product_cart.items():
                price = cheapest_shop.products[product]
                total = price * amount
                print(f"{amount} {product}s for {total} dollars")
                total_cost += total
            print(f"Total cost is {total_cost} dollars\nSee you again!")
            customer.money -= total_cost

            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now"
                  f" has {round(customer.money, 2)} dollars")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
