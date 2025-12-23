from app.configdata import load_config, create_shop, create_customers


def shop_trip() -> None:
    work_file = load_config()
    fuel_price = work_file["FUEL_PRICE"]

    customers = create_customers(work_file["customers"])
    shops = create_shop(work_file["shops"])

    for cust in customers:
        print(f"{cust.name} has {cust.money} dollars")

        shop_cost = {}
        shop_info = {}

        for shop in shops:
            (total_cost,
             purchase_info,
             product_cost) = cust.trip_cost(shop, fuel_price)
            shop_cost[shop.name] = total_cost
            shop_info[shop.name] = {
                "shop": shop,
                "info": purchase_info,
                "product_cost": product_cost
            }

            print(f"{cust.name}'s trip to the {shop.name} costs {total_cost}")

        if shop_cost:
            chippest_shop = min(shop_cost, key=shop_cost.get)
            cost_chippest_shop = shop_cost[chippest_shop]

            if cust.money >= cost_chippest_shop:
                shop_details = shop_info[chippest_shop]

                cust.move_to_shop(shop_details["shop"])

                cust.make_purchase(
                    shop_details["shop"],
                    shop_details["product_cost"],
                    shop_details["info"]
                )

                cust.money -= (cost_chippest_shop
                               - shop_details["product_cost"])

                cust.move_to_home()

                print(f"{cust.name} now has {cust.money:.2f} dollars\n")
            else:
                print(f"{cust.name} doesn't have "
                      f"enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
