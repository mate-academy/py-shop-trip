import datetime

from app.path import shops, customers
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip():
    shops_objects = []
    customers_objects = []
    for shop in shops:
        shops_objects.append(
            Shop(shop.get("name"), shop.get("location"), shop.get("products"))
        )

    for customer in customers:
        car_data = customer.get("car")
        car_name = car_data.get("brand")
        car_fuel = car_data.get("fuel_consumption")
        customers_objects.append(
            Customer(
                customer.get("name"),
                customer.get("product_cart"),
                customer.get("location"),
                customer.get("money"),
                Car(car_name, car_fuel),
            )
        )
    for customer in customers_objects:
        total = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_objects:
            ride_cost = 2 * customer.ride(shop.location)
            shop_cost = customer.shopping(shop)
            total_sum = ride_cost + shop_cost
            total.update({shop: total_sum})
            print(f"{customer.name}'s trip to the {shop.name} costs {total_sum:.2f}")
        cheapest_place = min(total.items(), key=lambda item: item[1])
        cheapest_shop_name = cheapest_place[0]
        if customer.money >= cheapest_place[1]:
            customer.move_to(cheapest_shop_name.location)
            customer.money -= cheapest_place[1]
            print(f"{customer.name} rides to {cheapest_shop_name.name}\n")
            time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {time_now}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            cheapest_shop_cost = 0
            for name, quan in customer.product_cart.items():
                price_per_item = cheapest_shop_name.products.get(name)
                cheapest_shop_cost += quan * price_per_item
                display_name = name + "s" if quan > 1 else name
                print(
                    f"{quan} {display_name} for {str(quan*price_per_item).rstrip('0').rstrip('.')} dollars"
                )

            print(f"Total cost is {cheapest_shop_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.move_to(customer.base_location)
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money to make a purchase in any shop"
            )
