class Spending:
    def __init__(self, fuel_price: float, fuel_consumption: float) -> None:
        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_costs(self, distance: float) -> float:
        total_distance = distance * 2
        return (total_distance * self.fuel_consumption / 100) * self.fuel_price

    def calculate_product_costs(
        self,
        customer_cart: dict,
        shop_products: dict
    ) -> float:
        total_cost = 0.0
        for product, quantity in customer_cart.items():
            total_cost += quantity * shop_products[product]
        return total_cost
