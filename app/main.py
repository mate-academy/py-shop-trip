from app.shops import Shop
from app.customers import Customer


def shop_trip():
    visitors = Customer.open_json_customers()
    for visitor in visitors:
        visitor.print_has_money()
        shops = Shop.open_json_shop()
        price = []
        for shop in shops:
            price.append(visitor.total_product_fuel_price(shop))
            print(f"{visitor.name}'s trip to the "
                  f"{shop.name} costs"
                  f" {visitor.total_product_fuel_price(shop)}")
        min_price = price.index(min(price))
        if visitor.money < visitor.total_product_fuel_price(shops[min_price]):
            return print(f"{visitor.name} doesn't have enough "
                         f"money to make purchase in any shop")
        shop_with_min_price = shops[min_price]
        home = visitor.location
        visitor.print_go_to_shop(shop_with_min_price)
        shop_with_min_price.print_the_bill(visitor)
        visitor.print_go_to_home()
        visitor.location = home
        print(visitor.print_change_balance(shop_with_min_price))
