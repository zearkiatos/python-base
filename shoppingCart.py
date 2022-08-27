

def get_more_expensive_product(shopping_cart: dict) -> str:
    more_expensive_price = None
    more_expensive_product = None
    expensive_product = 'There are not items in the cart'
    if (len(shopping_cart) > 0):
        for product in shopping_cart:
            if not more_expensive_price and not more_expensive_product:
                more_expensive_price = shopping_cart[product]
                more_expensive_product = product
            elif (more_expensive_price < shopping_cart[product] or (more_expensive_price == shopping_cart[product] and more_expensive_product.lower() > product.lower())):
                more_expensive_price = shopping_cart[product]
                more_expensive_product = product
        expensive_product = more_expensive_product

    return expensive_product


def get_shopping_cart_total_cost(shopping_cart: dict) -> float:
    total_cost = 0
    if (len(shopping_cart) > 0):
        for price in shopping_cart.values():
            total_cost += price

    return total_cost


shopping_cart = {
    'bananas': 1000,
    'candy': 10,
    'chocolates': 1000,
}

print(get_more_expensive_product(shopping_cart))

print(get_shopping_cart_total_cost(shopping_cart))
