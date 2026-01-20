import json
import app.customer as customer
import app.shop as shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = customer.make_list_customers(data)
    shops = shop.make_list_shops(data)
    all_prices = []
    chipest_shop = None

    for buyer in customers:
        buyer.has_money()
        for shop_variant in shops:
            variant = shop_variant.trip_costs(buyer.name,
                                              buyer.get_cost_trip,
                                              fuel_price,
                                              buyer.products_cart)
            all_prices.append(variant)
            if variant <= min(all_prices):
                chipest_shop = shop_variant
        if buyer.money >= min(all_prices):
            print(f"{buyer.name} rides to {chipest_shop.name}")
            print()
        else:
            print(f"{buyer.name} doesn't have enough money to make "
                  f"purchase in any shop")
            return
        cost_trip = buyer.get_cost_trip(chipest_shop.location, fuel_price)
        chipest_shop.give_purchase_receipt(buyer.name,
                                           min(all_prices),
                                           buyer.products_cart,
                                           cost_trip)
        buyer.count_remaining_money(min(all_prices))
        all_prices = []
