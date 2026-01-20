from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            money: float,
            used_fuel_in_dollars: float,
            location: list[int],
            product_carts: dict[str, int],
            car: Car
    ) -> None:
        self.name = name
        self.money = money
        self.used_fuel_in_dollars = used_fuel_in_dollars
        self.location = location
        self.product_carts = product_carts
        self.car = car


def make_customer_from_json_file(config_data: str) -> list[object]:
    customers = []
    for customer in config_data["customers"]:

        fuel_price = config_data.get("FUEL_PRICE", 0)
        fuel_consumption_in_dollars = (
            fuel_price * customer["car"]["fuel_consumption"]
        )

        product_carts = customer.get("product_cart", {})

        brand = customer["car"].get("brand", None)
        fuel_consumption = customer["car"].get("fuel_consumption", None)
        car = Car(brand, fuel_consumption)

        new_customer = (
            Customer(
                customer["name"],
                customer["money"],
                fuel_consumption_in_dollars,
                customer["location"],
                product_carts,
                car
            )
        )
        customers.append(new_customer)
    return customers
