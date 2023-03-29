from app.shop import Shops
from app.customer import Customers
from app.unpack_file import open_file


def shop_trip() -> None:
    for customer in open_file()["customer_list"]:
        one_customer = Customers(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        )
        one_customer.have_money()

        price_shop_trip = []
        for shop in open_file()["shop_list"]:
            one_shop = Shops(shop["name"], shop["location"], shop["products"])
            price_shop_trip.append(one_shop.total_price_trip(one_customer))

        best_shop = open_file()["shop_list"][
            price_shop_trip.index(min(price_shop_trip))
        ]

        if min(price_shop_trip) <= one_customer.money:
            best_shop = Shops(
                best_shop["name"],
                best_shop["location"],
                best_shop["products"]
            )
            print(f"{one_customer.name} rides to {best_shop.name}\n")

            best_shop.purchase_receipt(one_customer)
            best_shop.way_home(one_customer)

        else:
            print(
                f"{one_customer.name} doesn't have"
                f" enough money to make purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
