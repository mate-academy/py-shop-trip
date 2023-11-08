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

    def take_a_check(self, list_of_customer_param: list) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {list_of_customer_param[0]}, for your purchase!")
        print("You have bought: ")
        total = 0
        for key in self.products:
            cost = self.products[key] * list_of_customer_param[2][key]
            total += cost
            if int(cost) == cost:
                print(f"{list_of_customer_param[2][key]}"
                      f" {key}s for {int(cost)} dollars")
            else:
                print(f"{list_of_customer_param[2][key]}"
                      f" {key}s for {cost} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!")
