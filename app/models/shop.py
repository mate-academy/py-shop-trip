import datetime


class Shop:

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_a_check(
            self,
            name: str,
            request_prod: dict,
            check: dict
    ) -> None:
        total = check.pop("bill")
        print_check: str = (
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {name}, for your purchase!\n"
            f"You have bought: \n"
        )
        for product in check:
            print_check += (f"{request_prod[product]} "
                            f"{product}s for {check[product]} dollars\n")
        print_check += f"Total cost is {total} dollars\nSee you again!\n"
        print(print_check)
