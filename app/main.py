import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(R"C:\Users\Pavel\MateAcademy"
              R"\py-shop-trip\app\config.json", "r") as f:
        file_data = json.load(f)

    fuel_price = file_data["FUEL_PRICE"]
    customers = []
    shops = []
    for i in range(len(file_data["customers"])):
        customers.append(
            Customer(
                file_data["customers"][i]["name"],
                file_data["customers"][i]["product_cart"],
                file_data["customers"][i]["location"],
                file_data["customers"][i]["money"],
                Car(
                    file_data["customers"][i]["car"]["brand"],
                    file_data["customers"][i]["car"]["fuel_consumption"]
                ),
            )
        )

    for i in range(len(file_data["shops"])):
        shops.append(
            Shop(
                file_data["shops"][i]["name"],
                file_data["shops"][i]["location"],
                file_data["shops"][i]["products"]
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        best_trip = customer.calculate_fuel(
            customer.location,
            shops[0].location
        ) * fuel_price + customer.count_purchases(shops[0].products)
        best_shop_name = shops[0].name

        for shop in shops:
            transport_cost = customer.calculate_fuel(
                customer.location,
                shop.location
            ) * fuel_price
            products_cost = customer.count_purchases(shop.products)
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} cost "
                  f"{round(transport_cost + products_cost, 2)}")

            if best_trip > transport_cost + products_cost:
                best_trip = transport_cost + products_cost
                best_shop_name = shop.name

        if best_trip <= customer.money:
            print(f"{customer.name} rides to {best_shop_name}\n")

            for store in shops:
                if store.name == best_shop_name:
                    store.shop_print_receipt(customer)

            rest_customer_money = round(customer.money - best_trip, 2)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {rest_customer_money} dollars\n")
        else:
            print(f"{customer.name} doesn't have"
                  f" enough money to make purchase in any shop\n")


if __name__ == "__main__":
    shop_trip()
