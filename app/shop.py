from app.config_loader import load_config


data = load_config()

shop_lists = data["shops"]
shop_dicts = {key: info for key, info in enumerate(shop_lists)}

shop_product_carts = {
    key: info["products"]
    for key, info in shop_dicts.items()
}
