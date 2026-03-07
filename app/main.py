from app.customers import customers_to_class
from app.shop import shop_to_class


customers = customers_to_class("config.json")
shops = shop_to_class("config.json")

def shop_trip():
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            print(f"{customer.name}'s trip to the {shop.name} costs {customer.full_price(shop)}")
        best_choice = min(shops, key=lambda shop: customer.full_price(shop))
        if customer.money >= customer.full_price(best_choice):
            customer.go_to_shop(best_choice)
            best_choice.shop_receipt(customer.name, customer.product_cart)
            customer.go_home()
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop\n")

shop_trip()
