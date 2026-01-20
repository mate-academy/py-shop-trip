from .config_loader import load_config_data


def shop_trip() -> None:
    try:
        config_data = load_config_data("app/config.json")
    except Exception as e:
        print(f"Failed to load config file : {e}")
        return

    fuel_price = config_data["fuel_price"]
    customers = config_data["customers"]
    shops = config_data["shops"]

    for customer in customers:
        customer.go_shopping(shops, fuel_price)
