from app.logic import (prepare_for_shop_trip,
                       plan_shop_trip,
                       go_shopping)


def shop_trip() -> None:
    customers, shops = prepare_for_shop_trip()

    for customer in customers:
        if successful_plan := plan_shop_trip(customer, shops):
            go_shopping(customer, successful_plan)
