from app.distance import Distance
import datetime


class Customer:
    def __init__(self, customer: dict, costs = None, all_info: dict = None):
        self.customer = customer
        self.all_info = all_info
        self.costs = costs

    def price_for_1_km(self):
        consumption = self.customer["car"]["fuel_consumption"]
        return consumption / 100 * self.all_info["FUEL_PRICE"]

    def which_shop(self, shop_name: dict):
        prices = list(shop_name.values())
        names = list(shop_name)
        res = [True if self.customer["money"] < i else False for i in prices]
        if all(res):
            print(f"{self.customer['name']} doesn't have enough "
                  f"money to make purchase in any shop")
            return
        else:
            name = names[prices.index(min(prices))]
            print(f"{self.customer['name']} rides to {name}")

            def print_receipt():
                now = datetime.datetime.now()
                print(
                    f"\nDate: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"
                    f"Thanks, {self.customer['name']}, for you purchase!\n"
                    f"You have bought: "
                )
                customer_list = list(self.customer["product_cart"].values())
                products_name = list(self.customer["product_cart"])
                shop = list(self.all_info["shops"])
                sum_ = 0

                for i in range(len(customer_list)):
                    if name in list(shop[i].values()):
                        for j in range(len(list(shop[i]['products'].values()))):
                            cost = list(shop[i]['products'].values())
                            sum_ += customer_list[j] * cost[j]
                            print(f"{customer_list[j]}"
                                  f" {products_name[j]}s for "
                                  f"{customer_list[j] * cost[j]} dollars")
                print(f"Total cost is {sum_} dollars\n"
                      f"See you again!\n")

            print_receipt()
            print(f"{self.customer['name']} rides home\n"
                  f"{self.customer['name']} now has "
                  f"{self.customer['money'] - min(self.costs)} dollars\n")


class Shop:
    def __init__(
            self,
            shop: dict,
            dct: dict
    ):
        self._shop = shop
        self.dct = dct

    def cart_price_list(self, customer):
        customer_list = list(customer["product_cart"].values())
        shop_price_list = list(self._shop["products"].values())
        result = sum(
            [
                customer_list[i] * shop_price_list[i]
                for i in range(len(customer_list))
            ]
        )
        return result

    def trip_cost(self, customer):
        distance = Distance(
            customer["location"],
            self._shop["location"]
        ).distance()

        final_price = Shop.cart_price_list(self, customer)
        price_for_1_km = Customer(customer, all_info=self.dct).price_for_1_km()
        result = final_price + distance * price_for_1_km * 2

        return round(result, 2)
