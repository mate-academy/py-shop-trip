from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    customer_product_curt: dict
    shop: dict

    def buying_products(self) -> str:
        total = 0

        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for key, value in self.customer_product_curt.items():
            if key in self.shop:
                amount = value * self.shop[key]
                if amount - int(amount) == 0:
                    amount = int(amount)
                total += amount
                print(f"{value} {key}s for {amount} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
