import json

from car import Car
from customer import Customer
from shop import Shop


def price_of_gasoline(
    customer: Customer, shop: Shop, fuel_price: float
) -> float:
    km = (
        round(
            (
                (customer.location[0] - shop.location[0]) ** 2
                + (customer.location[1] - shop.location[1]) ** 2
            )
            ** 0.5,
            2,
        )
        * 2
    )
    price = (customer.car.fuel_consumption / 100 * km) * fuel_price
    return price


def products_price(customer: Customer, shop: Shop) -> float:
    return sum(
        customer.product_cart[product] * shop.products[product]
        for product in customer.product_cart.keys()
    )


def have_bought(customer: Customer, shop: Shop) -> None:
    for product in customer.product_cart:
        print(
            f"{customer.product_cart[product]} {product}s for "
            f"{customer.product_cart[product] * shop.products[product]} "
            f"dollars"
        )


def shop_trip() -> None:
    with open("config.json") as json_data:
        data = json.load(json_data)

        fuel_price = data["FUEL_PRICE"]
        customers_list = [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"],
                ),
            )
            for customer in data["customers"]
        ]
        shop_list = [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"],
            )
            for shop in data["shops"]
        ]
        prices_dict = {}

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shop_list:
            trip_price = round(
                price_of_gasoline(customer, shop, fuel_price)
                + products_price(customer, shop),
                3,
            )
            print(
                f"{customer.name}`s trip to the {shop.name} costs {trip_price}"
            )
            prices_dict.update({shop.name: trip_price})

        min_price = min([index for index in prices_dict.values()])
        shop_name = list(prices_dict.keys())[
            list(prices_dict.values()).index(min_price)
        ]

        if min_price > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            print(f"{customer.name} rides to {shop_name}\n")
            print(
                f"Date: 04/01/2021 12:33:41\n"
                f"Thanks, {customer.name}, for your purchase!\n"
                f"You have bought:"
            )

            shop_where_customer_go = [
                shop for shop in shop_list if shop.name == shop_name
            ][0]
            have_bought(customer, shop_where_customer_go)
            print(
                f"Total cost is "
                f"{products_price(customer, shop_where_customer_go)} dollars\n"
                f"See you again!\n"
            )
            print(
                f"{customer.name} rides home\n"
                f"{customer.name} now has "
                f"{customer.money - min_price} dollars\n"
            )


if __name__ == "__main__":
    shop_trip()
