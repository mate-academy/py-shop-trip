class Purchase:
    def __init__(self, data_file: dict) -> None:
        self.data = data_file

    def create_purchase(self, cheap_shop: dict, name: str) -> None:
        print("Date: 04/01/2021 12:33:41")
        chosen_shop = None
        total = 0
        for i in self.data["shops"]:
            if i["name"] == cheap_shop:
                chosen_shop = i
        for item in self.data["customers"]:
            milk_count = item["product_cart"]["milk"]
            bread_count = item["product_cart"]["bread"]
            butter_count = item["product_cart"]["butter"]
            if item["name"] == name:
                product_to_buy = chosen_shop["products"]
                print(f"Thanks, {item['name']}, for you purchase!")
                print("You have bought: ")
                print(
                    f"{milk_count} milks for "
                    f"{product_to_buy['milk'] * milk_count} dollars"
                )
                total += product_to_buy["milk"] * milk_count
                print(
                    f"{bread_count} breads for "
                    f"{product_to_buy['bread'] * bread_count} dollars"
                )
                total += product_to_buy["bread"] * bread_count
                print(
                    f"{butter_count} butters for "
                    f"{product_to_buy['butter'] * butter_count} dollars"
                )
                total += product_to_buy["butter"] * butter_count
                print(f"Total cost is {total} dollars")
                print("See you again!\n")
                print(f"{name} rides home")
