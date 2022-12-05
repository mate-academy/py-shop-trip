from app.data_export_from_json import customers_data_dictionary
from app.data_export_from_json import shops_data_dictionary


def shop_trip() -> None:
    for customer in customers_data_dictionary.values():
        customer.has_money()

        for shop in shops_data_dictionary.values():
            costs_per_shop = customer.shop_visiting_cost(shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {costs_per_shop}")

        ride_to_shop = customer.ride_to_shop(shops_data_dictionary)
        cost_effective_shop = customer.choose_shop(
            shops_data_dictionary
        )

        if ride_to_shop is True:
            print(f"{customer.name} rides to "
                  f"{cost_effective_shop.name}")
            print()
            customer.customer_purchasing_process(
                customer.choose_shop(shops_data_dictionary)
            )
        if ride_to_shop is False:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")


if __name__ == "__main__":
    shop_trip()
