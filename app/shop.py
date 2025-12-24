from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products_that_shop_provides: dict

    def products_cost(self, customer_cart: dict) -> int | float:
        total_cost = 0
        for name_products, quantity in customer_cart.items():
            if name_products in self.products_that_shop_provides:
                price_eah_one_product = \
                    self.products_that_shop_provides[name_products]
                cost = price_eah_one_product * quantity
                total_cost += cost
        return round(total_cost, 2)

    def print_receipt(self, customer_name: str, customer_cart: dict) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in customer_cart.items():
            if product in self.products_that_shop_provides:
                cost = self.products_that_shop_provides[product] * quantity
                if float(cost).is_integer():
                    print(f"{quantity} {product}s for {int(cost)} dollars")
                else:
                    print(f"{quantity} {product}s for {cost:.1f} dollars")
                total_cost += cost
        if float(total_cost).is_integer():
            print(f"Total cost is {int(total_cost)} dollars")
        else:
            print(f"Total cost is {total_cost:.1f} dollars")
        print("See you again!\n")
