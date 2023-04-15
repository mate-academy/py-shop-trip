import datetime


class Receipt:
    def __init__(
            self,
            customer_name: str,
            shop_name: str,
            purchase_list: dict,
            total_cost: float
    ) -> None:
        self.customer_name = customer_name
        self.shop_name = shop_name
        self.purchase_list = purchase_list
        self.total_cost = total_cost
        self.timestamp = datetime.datetime.now()

    def __str__(self) -> str:
        purchase_str = "\n".join(
            [f"{value} {key}s for {price} dollars"
             for key, (value, price) in self.purchase_list.items()]
        )
        return (f"Date: {self.timestamp.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Thanks, {self.customer_name}, for your purchase!\n"
                f"You have bought:\n{purchase_str}\n"
                f"Total cost is {self.total_cost} dollars\n"
                f"See you again!\n")
