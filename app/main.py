from app.customer import Customer
from app.shop import Shop
from app.shopping import Shopping


def shop_trip() -> None:
    shopping_day = Shopping.from_json_file("app/config.json")
    Customer.fuel_price = shopping_day.FUEL_PRICE
    customers = [
        Customer.from_dict(person) for person in shopping_day.customers
    ]
    shops = [Shop.from_dict(store) for store in shopping_day.shops]
    for customer in customers:
        shop = customer.choose_shop(shops)
        if shop:
            customer.buy_at_shop(shop)


print(shop_trip())
