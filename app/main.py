import json
import os


def shop_trip() -> None:
    from app.car import Car
    from app.shop import Shop
    from app.customer import Customer

    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as f:
        data = json.load(f)

    customers = []
    for cus in data["customers"]:
        car = Car(cus["car"]["brand"], cus["car"]["fuel_consumption"])
        customers.append(Customer(
            name=cus["name"],
            location=cus["location"],
            product_cart=cus["product_cart"],
            money=cus["money"],
            car=car
        ))

    shops = [Shop(**s) for s in data["shops"]]
    fuel_price = data["FUEL_PRICE"]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_price = float("inf")
        best_shop = None

        for shop in shops:
            distance = customer.calculate_distance(shop)
            one_way = customer.car.calculate_fuel_cost(distance, fuel_price)
            road = one_way * 2
            purchase_cost = 0

            for product_name, quantity in customer.product_cart.items():
                price = shop.products[product_name]
                purchase_cost += price * quantity
            total_price = purchase_cost + road

            if total_price < best_price:
                best_price = total_price
                best_shop = shop
            print(f"{customer.name}'s trip to the {shop.name} costs "
                  f"{round(total_price, 2)}")

        if best_price <= customer.money:
            customer.move_to_shop(best_shop)
            print()
            best_shop.print_bill(customer)
            print()
            customer.move_to_home()
            customer.money -= best_price
            print(f"{customer.name} now has {round(customer.money, 2)} "
                  f"dollars")
            print()
        else:
            print(f"{customer.name} doesn't have enough money to make "
                  f"a purchase in any shop")
