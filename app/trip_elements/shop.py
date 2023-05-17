import datetime
from app.trip_elements.customer import Customer


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def cart_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for item in product_cart:
            total_cost += self.products[item] * product_cart[item]
        return total_cost

    def shop_visit(self, customer: Customer) -> None:
        cart = customer.product_cart
        total_cost = 0
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for product, cost in self.products.items():
            product_cost = cart[product] * cost
            total_cost += product_cost
            print(f"{cart[product]} {product}s for {product_cost} dollars")
        customer.money -= total_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    def total_trip_cost(self, fuel_cost: float, customer: Customer) -> float:
        gasoline_cost = customer.car.gasoline_calculation(
            fuel_cost,
            self.location,
            customer.location
        ) * 2
        cart_cost = self.cart_cost(customer.product_cart)
        return round(gasoline_cost + cart_cost, 2)
