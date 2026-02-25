from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def products_cost(self, customer_products: dict) -> float:
        cost = 0.0
        for product, quantity in customer_products.items():
            cost += quantity * self.products[product]
        return cost

    def products_cost_with_command(self, customer_products: dict) -> float:
        cost = 0.0
        for product, quantity in customer_products.items():
            cost = quantity * self.products[product]
            if cost.is_integer():
                cost = int(cost)
            print(f"{quantity} {product}s for {cost:.2f} dollars")
        total_cost = self.products_cost(customer_products)
        print(f"Total cost is {total_cost:.2f} dollars")
        return total_cost
