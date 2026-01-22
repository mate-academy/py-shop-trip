from app.types.types import (
    ConfigData,
    CustomerData,
    ShopData,
)


def extract_config_values(
    config: ConfigData,
) -> tuple[float, list[CustomerData], list[ShopData]]:
    try:
        fuel_price = config["FUEL_PRICE"]
        customers_data = config["customers"]
        shops_data = config["shops"]
    except KeyError as e:
        raise KeyError(f"Missing required config key: {e}") from e
    else:
        return fuel_price, customers_data, shops_data
