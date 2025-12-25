from app.data.location import Location
from app.data.product_cart import ProductCart


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = Location(*location)
        self.products_price = ProductCart(**products)

    def cost_in_store(self, customer: object, fuel_cost: float) -> float:
        result_price = fuel_cost
        shop_prod = self.products_price.products
        cust_cart = customer.product_cart.products
        for prod in shop_prod:
            result_price += shop_prod[prod] * cust_cart[prod]
        print(f"{customer.name}'s trip to the "
              f"{self.name} costs "
              f"{result_price:.2f}")
        return result_price
