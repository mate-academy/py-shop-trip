from app.customers import customers_to_class
from app.shop import shop_to_class


def shop_trip() -> None:
    customers = customers_to_class("config.json")
    shops = shop_to_class("config.json")

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            print(f""
                  f"{customer.name}'s trip to the "
                  f"{shop.name} costs {customer.full_price(shop)}"
                  )
        best_choice = min(shops, key=lambda shop: customer.full_price(shop))
        if customer.money >= customer.full_price(best_choice):
            print(customer.go_to_shop(best_choice))
            print(best_choice.shop_receipt(
                customer.name,
                customer.product_cart
            ))
            print(customer.go_home())
        else:
            print(f""
                  f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop"
                  f"\n")
