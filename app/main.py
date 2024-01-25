from app.objects.car import Car
from app.objects.customer import Customer
from app.objects.shop import Shop
from app.data.json_extraction import extract_data


data = extract_data()

FUEL_PRICE = data["FUEL_PRICE"]
customers = data["customers"]
shops = data["shops"]

customers = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
    )
    for customer in customers
]

shops = [
    Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    )
    for shop in shops
]


def shop_trip() -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            customer.trip_choice(shop, FUEL_PRICE)

        if customer.money < customer.min_trip_cost:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return

        print(f"{customer.name} rides to {customer.shop_choice.name}")
        customer.shop_choice.print_receipt(customer.name,
                                           customer.product_cart)

        print(f"{customer.name} rides home")

        customer.money -= customer.min_trip_cost
        print(f"{customer.name} now has {customer.money} dollars\n")
