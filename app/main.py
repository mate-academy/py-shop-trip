import os

from app.data_read import DataRead


def shop_trip() -> None:
    config_file = "config.json"
    file_path = os.path.abspath(__file__)
    config_file_path = os.path.join(os.path.dirname(file_path), config_file)

    data_read = DataRead(config_file_path)
    customers = data_read.get_customers()
    shops = data_read.get_shops()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer_trips_prices = []
        for shop in shops:
            total_product_price = shop.check_cost_products(
                customer.product_cart
            )

            distance = customer.car.calculate_distance(
                customer.location,
                shop.location
            )
            road_cost = customer.car.road_cost(
                distance,
                data_read.get_fuel_price())

            total_cost = road_cost + total_product_price
            print(f"{customer.name}'s trip to the {shop.name} costs "
                  f"{total_cost}")

            customer_trips_prices.append((shop, total_cost))

        cheapest_shop, cheapest_price = min(
            customer_trips_prices,
            key=lambda x: x[1]
        )
        store_receipt = cheapest_shop.get_store_receipt(customer)

        if cheapest_price > customer.money:
            print(f"{customer.name} doesn't have enough money to make "
                  f"a purchase in any shop")
            continue
        customer.spend_money(cheapest_price)

        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        print(store_receipt)

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars\n")


if __name__ == "__main__":
    shop_trip()
