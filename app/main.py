from app.customer import Customer
from app.shop import Shop
from app.loading_data import loading_data


def shop_trip() -> None:

    loading_data()

    for customer in Customer.customers:
        customer.print_amount_of_money()

        customer.find_cheapest_shop_trip(Shop.shops)

        if customer.cheapest_shop_trip is not None:
            customer.ride_to_shop()
            customer.get_purchase_receipt(customer.cheapest_shop_trip.products)
            customer.ride_to_home_and_check_money()
        else:
            customer.print_not_enough_money()


if __name__ == "__main__":
    shop_trip()
