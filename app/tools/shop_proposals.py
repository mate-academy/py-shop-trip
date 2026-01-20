from app.classes.customer import Customer
from app.classes.shop import Shop


def propose(
        customer: Customer,
        shops: list[Shop],
        fuel_price: float
) -> tuple[Shop, float, float]:
    shop_proposals = {}

    for shop in shops:

        shop_proposals[shop] = (shop.calc_shop_path(customer, fuel_price)
                                + shop.calc_cost_cart(customer))

        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {shop_proposals[shop]}")

    best_shop = min(shop_proposals.items(), key=lambda item: item[1])[0]
    path_price = best_shop.calc_shop_path(customer, fuel_price)
    bill = best_shop.calc_cost_cart(customer)
    return best_shop, path_price, bill
