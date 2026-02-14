# flake8: noqa: *
from app.calculate import calculate_products, calculate_distance
from app.parser import parser


def shop_trip() -> None:
    config_file = parser("app/config.json")
    fuel_price, customers, shops = config_file
    for customer in customers:
        customer_location = customer.location.copy()
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        best_price = 0
        for shop in shops:
            new_price = calculate_products(customer, shop) + calculate_distance(customer, shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {new_price:.2f}")
            if best_shop is None or new_price < best_price:
                best_shop = shop
                best_price = new_price
        if customer.money >= best_price:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.money -= best_price
            best_shop.customer_purchase(customer)
            customer.location = best_shop.location.copy()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
            customer.location = customer_location.copy()
            continue
        print(f"{customer.name} doesn't have enough money to make a purchase in any shop")