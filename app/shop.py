import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def costs_trip(
            self,
            cost_fuel_to_shop: float,
            product_list_customer: dict
    ) -> None:
        sum_products = 0
        for key in product_list_customer:
            if key in self.products:
                sum_products += self.products[key] * product_list_customer[key]
        return (cost_fuel_to_shop * 2) + sum_products

    def customer_in_magazine(
            self,
            name: str,
            product_list_customer: dict
    ) -> None:
        key_list_customer = [key for key in product_list_customer]
        date = datetime.datetime.now()
        formatted_date = date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        list_price = []
        for key in key_list_customer:
            result = product_list_customer[key] * self.products[key]
            if float(result).is_integer():
                result = int(result)
            else:
                result = result
            list_price.append(result)
            print(f"{product_list_customer[key]} {key}s for {result} dollars")
        print(f"Total cost is {sum(list_price)} dollars")
        print("See you again!\n")
