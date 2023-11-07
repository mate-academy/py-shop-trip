import math

from app.customer import Customer


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop.get("name")
        self.location = shop.get("location")
        self.product_price = shop.get("products")

    def calculate_fuel_price(
            self,
            customer: Customer,
            fuel_price: int | float
    ) -> int | float:
        customer_location_x, customer_location_y = customer.location
        shop_location_x, shop_location_y = self.location
        pow_x = math.pow(shop_location_x - customer_location_x, 2)
        pow_y = math.pow(shop_location_y - customer_location_y, 2)
        trip = math.sqrt(pow_x + pow_y) * 2
        consumption_1km = customer.car.fuel_consumption / 100
        return round(trip * consumption_1km * fuel_price, 2)

    def calculate_trip_price(
            self,
            customer: Customer,
            fuel_price: float | int
    ) -> int | float:
        price = 0
        for product in customer.product_cart:
            if product in self.product_price:
                customer_product = customer.product_cart[product]
                price += customer_product * self.product_price.get(product)
        price += self.calculate_fuel_price(customer, fuel_price)
        return price

    def shop_receipt(self, customer: Customer) -> None:
        print(f"Date: 04/01/2021 12:33:41\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought: ")
        total_amount = 0
        for product in customer.product_cart:
            product_amount = customer.product_cart[product]
            amount = product_amount * self.product_price[product]
            if isinstance(amount, float):
                if str(amount)[-1] == "0":
                    amount = int(amount)
            print(f"{product_amount} {product}s for "
                  f"{amount} dollars")
            total_amount += amount
        print(f"Total cost is {total_amount} dollars\n"
              f"See you again!\n")
