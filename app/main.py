from app.config_loader import ConfigLoader
from app.presentation.shopping_presenter import ShoppingPresenter
from app.services.calculate_shopping_results import (
    calculate_customer_shopping_results
)
from app.services.calculate_purchase_receipt import (
    calculate_customer_purchase_receipt
)


def shop_trip() -> None:
    config = ConfigLoader()
    presenter = ShoppingPresenter()

    shopping_results = calculate_customer_shopping_results(
        config.customers,
        config.shops,
        config.fuel_price,
    )

    for customer_result in shopping_results:

        presenter.display_customer_shopping_result(customer_result)

        if customer_result.lowest_total_cost_shop is None:
            continue

        purchase_receipt = calculate_customer_purchase_receipt(
            customer_result.customer,
            customer_result.lowest_total_cost_shop,
        )

        presenter.display_purchase_receipt(
            customer_result.customer,
            purchase_receipt,
        )

        print(f"{customer_result.customer.name} rides home")
        print(f"{customer_result.customer.name} now "
              f"has {customer_result.money_after_purchase} dollars\n")
