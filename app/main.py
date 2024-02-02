from app.objects.car import Car
from app.objects.customer import Customer
from app.objects.shop import Shop
from app.data.json_extraction import extract_data


def shop_trip() -> None:
    data = extract_data()

    fuel_price = data["FUEL_PRICE"]
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

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop_choice, trip_cost = customer.find_cheapest_trip(shops, fuel_price)

        if customer.money < trip_cost:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return

        print(f"{customer.name} rides to {shop_choice.name}")
        shop_choice.print_receipt(customer.name,
                                  customer.product_cart)

        print(f"{customer.name} rides home")

        customer.money -= trip_cost
        print(f"{customer.name} now has {customer.money} dollars\n")
