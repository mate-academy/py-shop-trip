from app.models.shop.shopping_result import ShoppingResult
from app.models.customer.customer import Customer
from app.models.purchase.purchase_receipt_generator import (
    PurchaseReceiptGenerator
)


class ShoppingPresenter:
    @staticmethod
    def display_customer_shopping_result(
            customer_result: ShoppingResult
    ) -> None:
        print(f"{customer_result.customer.name} "
              f"has {customer_result.customer.money} dollars")

        for shop_name, cost \
                in customer_result.shopping_options.items():
            print(f"{customer_result.customer.name}'s "
                  f"trip to the {shop_name} costs {cost}")

        if customer_result.lowest_total_cost_shop is None:
            print(f"{customer_result.customer.name} "
                  "doesn't have enough money to make a purchase in any shop")
            return

        print(f"{customer_result.customer.name} "
              f"rides to {customer_result.lowest_total_cost_shop.name}")

    @staticmethod
    def display_purchase_receipt(
            customer: Customer,
            receipt: PurchaseReceiptGenerator
    ) -> None:
        print(f"\nDate: {receipt.purchase_date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for item in receipt.bought_products:
            print(f"{item.quantity:g} {item.product}s "
                  f"for {item.product_cost:g} dollars")

        print(f"Total cost is {receipt.total_cost} dollars")
        print("See you again!\n")
