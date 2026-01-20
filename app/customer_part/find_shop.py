from app.customer_part.customer import Customer
from app.shop_part.shop import Shop


def find_cheapest_shop(
    customers: list[Customer], shops: list[dict[Shop]]
) -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.option = None
        for shop_object in shops:
            for shop in shop_object.values():
                product_price = Shop.calculate_products_total_price(
                    customer.cart, shop.products
                )
                fuel_price = customer.car.make_fuel_calculation(
                    customer.location, shop.location
                )
                total_price = Shop.calculate_products_total_price(
                    customer.cart, shop.products
                ) + customer.car.make_fuel_calculation(
                    customer.location, shop.location
                )
                print(
                    f"{customer.name}'s trip to the "
                    f"{shop.name} costs {total_price}"
                )
                if (
                    customer.option is None
                    or customer.option.get("total_price") > total_price
                ):
                    customer.option = {
                        "shop_object": shop,
                        "products_price": product_price,
                        "fuel_price": fuel_price,
                        "total_price": total_price,
                    }
            if customer.money >= customer.option.get("total_price"):
                print(
                    f"{customer.name} rides to "
                    f"{customer.option.get('shop_object').name}\n"
                )
                customer.option.get("shop_object").take_payment(customer)
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has {customer.money} dollars\n")
            else:
                print(
                    f"{customer.name} doesn't have enough "
                    f"money to make a purchase in any shop"
                )
