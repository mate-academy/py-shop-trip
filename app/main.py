import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(
            "./app/config.json",
            "rb"
    ) as json_file:

        data_from_file = json.load(json_file)
        fuel_price = data_from_file["FUEL_PRICE"]
        for customer in data_from_file["customers"]:
            current_car = Car(fuel_price, customer["car"])
            current_customer = Customer(customer)
            current_customer.get_money_info()
            for shop in data_from_file["shops"]:
                current_shop = Shop(shop)
                cost_trip_by_car = current_car.count_cost_of_trip(
                    current_customer,
                    current_shop
                )

                purchase_price = current_shop.count_purchase_price(
                    current_customer.product_cart
                )

                total_spends = cost_trip_by_car + purchase_price
                Shop.shop_list.append((current_shop, total_spends))
                print(f"{current_customer.name}'s trip to the "
                      f"{current_shop.name} costs {total_spends}")

            cheapest_shop, cheapest_cost = Shop.find_the_cheapest_shop()
            if cheapest_cost <= current_customer.money:
                print(f"{current_customer.name} rides to "
                      f"{cheapest_shop.name}\n")

                cheapest_shop.customer_visit(
                    current_customer.name,
                    current_customer.product_cart
                )

                print(f"{current_customer.name} rides home")
                remainder = (current_customer.money - cheapest_cost)
                print(f"{current_customer.name} now has {remainder} dollars\n")
            else:
                print(f"{current_customer.name} doesn't have enough money "
                      f"to make a purchase in any shop")
