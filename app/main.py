import os
import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, 'config.json')

    try:
        with open(config_path) as config_file:
            config: dict = json.load(config_file)
    except FileNotFoundError:
        print("Error: Config file 'config.json' not found.")
        return

    fuel_price: float = config.get("FUEL_PRICE", 0)

    customers: list[Customer] = [create_customer(customer_data) for customer_data in config.get("customers", [])]
    shops: list[Shop] = [create_shop(shop_data) for shop_data in config.get("shops", [])]

    for customer in customers:
        trip_costs: list[tuple[Shop, float]] = [(shop, customer.calculate_trip_cost(shop, fuel_price)) for shop in
                                                shops]
        if not trip_costs:
            print("Error: No shops found.")
            return

        cheapest_shop, cheapest_cost = min(trip_costs, key=lambda x: x[1])

        print(f"{customer.name} has {customer.money} dollars in any shop")
        print(f"{customer.name}'s trip to the {cheapest_shop.name} costs {cheapest_cost:.2f}")

        if customer.money >= cheapest_cost:
            customer.update_location(cheapest_shop.location)
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer_purchase_cost = sum(
                customer.product_cart[item] * cheapest_shop.products[item] for item in customer.product_cart)
            cheapest_shop.generate_purchase_receipt(customer.name, customer.product_cart, customer_purchase_cost)
            cheapest_shop.update_product_quantities(customer.product_cart)
            customer.money -= customer_purchase_cost
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


def create_customer(customer_data: dict) -> Customer:
    car_data: dict = customer_data.get("car", {})
    car: Car = Car(car_data.get("brand", ""), car_data.get("fuel_consumption", 0))
    return Customer(customer_data.get("name", ""), customer_data.get("product_cart", {}),
                    customer_data.get("location", []), customer_data.get("money", 0), car)


def create_shop(shop_data: dict) -> Shop:
    return Shop(shop_data.get("name", ""), shop_data.get("location", []), shop_data.get("products", {}))


if __name__ == "__main__":
    shop_trip()
