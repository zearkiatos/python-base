MAX_PRICE_TO_CHOOSE = 10000


def get_chepest_product(product_catalog: dict) -> str:
    chepest_price = None
    chepest_product = None
    if len(product_catalog) > 0:
        for product in product_catalog:
            if not chepest_price and not chepest_product:
                chepest_price = product_catalog[product]
                chepest_product = product
            elif (chepest_price > product_catalog[product] or (chepest_price == product_catalog[product] and chepest_product.lower() > product.lower())):
                chepest_price = product_catalog[product]
                chepest_product = product
        if chepest_price > MAX_PRICE_TO_CHOOSE:
            chepest_product = None
    else:
        chepest_product = 'There are not products to choose'
    
    return chepest_product
            


product_catalog = {
    'skirt': 1000,
    "pajama": 500,
    "iphone": 10000,
    "t-shirt": 2000,
    "shoes": 3000,
    "earing": 200,
    "ring": 200
}

print(get_chepest_product(product_catalog))