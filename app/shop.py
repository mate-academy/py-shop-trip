from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    inventory: dict

    def bill(self, order: dict) -> tuple:
        sum_order = 0
        bill = list()
        for product, amt in order.items():
            if self.inventory.get(product):
                price_amt = self.inventory[product] * amt
                sum_order += price_amt
                if isinstance(price_amt, float) and price_amt.is_integer():
                    price_amt = int(price_amt)
                bill.append(f"{amt} {product}s for {price_amt} dollars")
            else:
                print(product, "not in stack")
                return 0, 0
        return round(sum_order, 2), bill
