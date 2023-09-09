class CustomerCar:
    def __init__(self, name_customer: dict) -> None:
        self.name_customer = name_customer

    def customer_location(self) -> dict:
        fuel_consumption_car = (
            self.name_customer.get("car").get("fuel_consumption")
        )
        distance_customer_x = self.name_customer.get("location")[0]
        distance_customer_y = self.name_customer.get("location")[1]
        quantities = self.name_customer.get("product_cart")
        money = self.name_customer.get("money")
        product = self.name_customer.get("product_cart")
        name = self.name_customer.get("name")
        print(f"{name} has {money} dollars")
        return {
            "fuel_consumption_car": fuel_consumption_car,
            "distance_customer_x": distance_customer_x,
            "distance_customer_y": distance_customer_y,
            "quantities": quantities,
            "money": money,
            "product": product,
            "name": name,
        }
