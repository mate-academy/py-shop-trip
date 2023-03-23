import datetime
from app.customer import Customer
from app.shop import Shop
from app.export_data import export_data


def shop_trip() -> None:

    export_data()

    customers = Customer.customer_list
    shops = Shop.shop_list
    for customer in customers:
        nears_shop = ""
        print(customer)
        cost_trip = customer.money
        for shop in shops:
            trip_to_shop = shop.cost_for_fuel(customer.location, customer.car)\
                + shop.products_cost(customer.product_cart)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_to_shop}")
            if trip_to_shop < cost_trip:
                cost_trip = trip_to_shop
                nears_shop = shop
        if cost_trip == customer.money:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
            return
        print(f"{customer.name} rides to {nears_shop.name}\n")
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for product, count in customer.product_cart.items():
            print(f"{count} {product}s for "
                  f"{count * nears_shop.products[product]} dollars")
        print(f"Total cost is "
              f"{round(nears_shop.products_cost(customer.product_cart), 2)}"
              f" dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - cost_trip} dollars\n")
