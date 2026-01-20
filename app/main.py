from app.transfer import transfer
from math import hypot


def shop_trip() -> None:
    fuel_price, list_customers, list_shops = transfer()
    for customer in list_customers:
        shop_list = []
        print(f"{customer.name} has {customer.money} dollars")
        for shop in list_shops:
            car_fuel_1km = customer.car.fuel / 100
            loc1 = customer.location
            loc2 = shop.location
            dist = hypot(loc2[0] - loc1[0], loc2[1] - loc1[1])
            cost_travel = round(dist * car_fuel_1km * fuel_price * 2, 2)
            cost_products = sum(customer.product_cart[key] * shop.products[key]
                                for key in shop.products)
            costs = cost_products + cost_travel
            print(f"{customer.name}'s trip to the {shop.name} costs {costs}")
            shop_list.append((shop, costs))
        customer_choice = min(shop_list, key=lambda x: x[1])
        if customer.money < customer_choice[1]:
            print(customer.name,
                  "doesn't have enough money to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {customer_choice[0].name}")
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        shop_choice = customer_choice[0].products
        costs = 0
        for key in customer.product_cart:
            costs += (customer.product_cart[key] * shop_choice[key])
            total = customer.product_cart[key] * shop_choice[key]
            if total == int(total):
                total = int(total)
            print(f"{customer.product_cart[key]} {key}s for {total} dollars")
        print(f"Total cost is {costs} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        new_balance = customer.money - customer_choice[1]
        print(f"""{customer.name} now has {new_balance} dollars""")
        print()


if __name__ == "__main__":
    shop_trip()
