from app.config_loader import load_config


data = load_config()

customers_lists = data["customers"]
customers_dicts = {key: info for key, info in enumerate(customers_lists)}

product_carts = {
    i: value["product_cart"]
    for i, value in customers_dicts.items()
}
