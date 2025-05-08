class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, cart: dict) -> float:
        total_cost = 0
        for item, quantity in cart.items():
            if item in self.products:
                total_cost += self.products[item] * quantity
        return total_cost

    def print_receipt(self, current_time: str, cust_name: str,
                      total_cost: float, cart: dict) -> None:
        """Print a formatted receipt with purchase details"""
        print(f"Date: {current_time}")
        print(f"Thanks, {cust_name}, for your purchase!")
        print("You have bought:")
        for item, quantity in cart.items():
            if item in self.products:
                price = self.products[item] * quantity
                print(f"{quantity} {item}s "
                      f"for {int(price) if price.is_integer() else price}"
                      f" dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
