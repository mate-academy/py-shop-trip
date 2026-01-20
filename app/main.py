from app.dataset.customers import get_all_customers
from app.expenses.message import expanses_report
from app.dataset.shops import get_all_shops


def shop_trip() -> None:
    customers = get_all_customers()
    shops = get_all_shops()
    for customer in customers:
        expanses_report(customer, shops)


shop_trip()
