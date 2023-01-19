import dataclasses


@dataclasses.dataclass
class Shop:
    shop_name: str
    location_shop: list
    products_price: dict

    def calculate_product(self, product_cart: dict) -> dict:
        result = {}
        for product in self.products_price.keys():
            result[product] = (product_cart[product]
                               * self.products_price[product])
        return result

    @staticmethod
    def sum_of_products(products: dict) -> float:
        sum_products = 0
        for product in products.values():
            sum_products += product
        return sum_products
