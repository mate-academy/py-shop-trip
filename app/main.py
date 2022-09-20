import json
from app.customer import Customer, Shop


def shop_trip():
    with open("app/config.json", "r") as f:
        configuration = json.load(f)
        fuel_price = configuration["FUEL_PRICE"]
        for s in configuration["shops"]:
            Shop(s["name"], s["location"], s["products"])
        customers = []
        for c in configuration["customers"]:
            customer = Customer(
                c["name"],
                c["product_cart"],
                c["location"],
                c["money"],
                c["car"]["fuel_consumption"]
            )
            customers.append(customer)
        for customer in customers:
            shop = customer.shop_selection(fuel_price)
            if shop is not None:
                customer.buy_products(shop)
                customer.back_home()
