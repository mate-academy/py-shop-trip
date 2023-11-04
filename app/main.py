from app.data_configuration import Data


def shop_trip() -> None:
    data = Data()

    for customer in data.customers:

        shop, text = customer.choose_shop(data.shops, data.fuel_price)
        print(text)
        if shop:
            print(shop.sell_products(customer.name, customer.prod_cart))
            print(customer.drives_home())
