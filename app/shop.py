from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict,
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase_price(self, customer: Customer) -> float:
        price = 0
        for product in customer.product_cart:
            if product in self.products:
                price += (customer.product_cart[product]
                          * self.products[product])
        return price
