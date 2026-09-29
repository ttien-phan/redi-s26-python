def process_prices(prices, func):
    new_prices = []
    for price in prices:
        new_prices.append(func(price))

    return new_prices

prices = [10, 20, 50]

disc = process_prices(prices, lambda price : price * 0,8)

