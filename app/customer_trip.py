import json
from math import dist
import datetime
from app.costs import Costs


class Trip:
    @staticmethod
    def open_file(file_name: str) -> dict:
        with open(file_name, "r") as j_son:
            data = json.load(j_son)
        return data

    @staticmethod
    def transform_in_plural(data: list[str]) -> list:
        return [element + "s" for element in data]

    @staticmethod
    def customer_trip(data: dict) -> None:
        # Loop of customers data.
        for customer in data["customers"]:
            name = customer["name"]
            best_cost = []
            totals_of_shop = []
            print(f"""{name} has {customer["money"]} dollars""")

            # Loop of shop data.
            for index, shop in enumerate(data["shops"]):
                fuel_cons = customer["car"]["fuel_consumption"]
                distance = dist(tuple(customer["location"]),
                                tuple(shop["location"]))
                cost_trip = Costs.cost_of_trip(distance,
                                               fuel_cons,
                                               data["FUEL_PRICE"])
                total_eval = (cost_trip * 2
                              + Costs.check_money(customer["product_cart"],
                                                  shop["products"]))
                totals_of_shop.append(total_eval)

                # Check best prise considering car trip.
                if index == 0:
                    best_cost.append(total_eval)
                    best_cost.append(index)
                elif total_eval < best_cost[0]:
                    best_cost[0] = total_eval
                    best_cost[1] = index
                print(f"""{name}'s trip to the {shop["name"]} """
                      f"""costs{total_eval: .2f}""")

            # Check the possibility to perform purchase for all customer.
            if (customer["money"] < best_cost[0]
                    + Costs.check_money(
                        customer["product_cart"],
                        data["shops"][best_cost[1]]["products"])):
                print(f"{name} doesn't have enough money to make a"
                      f" purchase in any shop")
                return
            else:
                shop_name = data["shops"][best_cost[1]]["name"]
                print(f"{name} rides to {shop_name}")
                customer["location"] = data["shops"][best_cost[1]]["location"]

            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"\nDate: {date}\nThanks, {name}, "
                  f"for your purchase!\nYou have bought:")

            # Convert to plural the list of "product cart".
            list_prod = Trip.transform_in_plural(
                list(customer["product_cart"].keys())
            )

            # Loop for each product inside "product cart".
            total_cost = 0
            best_price = totals_of_shop[best_cost[1]]
            for index, product in enumerate(
                    list(customer["product_cart"].items())
            ):
                s_product = data["shops"][best_cost[1]]["products"][product[0]]
                product_cost = (product[1] * s_product)
                total_cost += product_cost
                if (isinstance(product_cost, float)
                        and str(product_cost).split(".")[1] == "0"):
                    product_cost = int(product_cost)
                print(f"{product[1]} {list_prod[index]} for "
                      f"{product_cost} dollars")
            print(f"Total cost is {total_cost} dollars\nSee you again!\n")
            print(f"{name} rides home\n{name} now has"
                  f"{(customer["money"] - best_price): .2f}"
                  f" dollars\n")
