from app.distance import Distance
import datetime


class Shop:

    def __init__(
            self,
            customer: dict,
            shop: dict,
            dct: dict
    ):
        self._customer = customer
        self._shop = shop
        self._dct = dct

    def price_for_1_km(self):
        consumption = self._customer["car"]["fuel_consumption"]
        return consumption / 100 * self._dct["FUEL_PRICE"]

    def cart_price_list(self):
        customer_list = list(self._customer["product_cart"].values())
        shop_price_list = list(self._shop["products"].values())
        result = sum(
            [
                customer_list[i] * shop_price_list[i]
                for i in range(len(customer_list))
            ]
        )
        return result

    def trip_cost(self):
        distance = Distance(
            self._customer["location"],
            self._shop["location"]
        ).distance()

        final_price = Shop.cart_price_list(self)
        price_for_1_km = Shop.price_for_1_km(self)
        result = final_price + distance * price_for_1_km * 2

        return round(result, 2)


class WhichShop(Shop):
    def __init__(
            self,
            costs: list,
            customer: dict,
            shop_name: dict,
            shop: dict,
            dct: dict
    ):
        super().__init__(customer, shop, dct)
        self._shop_name = shop_name
        self._costs = costs

    def which_shop(self):
        prices = list(self._shop_name.values())
        names = list(self._shop_name)
        res = [True if self._customer["money"] < i else False for i in prices]
        if all(res):
            print(f"{self._customer['name']} doesn't have enough "
                  f"money to make purchase in any shop")
            return
        else:
            now = datetime.datetime.now()
            name = names[prices.index(min(prices))]
            print(f"{self._customer['name']} rides to {name}")

        def receipt():
            print(
                f"\nDate: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Thanks, {self._customer['name']}, for you purchase!\n"
                f"You have bought: "
            )
            customer_list = list(self._customer["product_cart"].values())
            products_name = list(self._customer["product_cart"])
            shop = list(self._dct["shops"])
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

        receipt()
        print(f"{self._customer['name']} rides home\n"
              f"{self._customer['name']} now has "
              f"{self._customer['money'] - min(self._costs)} dollars\n")
