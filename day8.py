def max_profit(prices):
    if not prices:
        return 0, -1, -1

    min_price = prices[0]
    buy_day = 0

    max_profit = 0
    best_buy_day = 0
    best_sell_day = 0

    for i in range(1, len(prices)):

        # Update minimum price
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i

        # Calculate profit if selling today
        profit = prices[i] - min_price

        if profit > max_profit:
            max_profit = profit
            best_buy_day = buy_day
            best_sell_day = i

    return max_profit, best_buy_day, best_sell_day


# Example
prices = [7, 1, 5, 3, 6, 4]

profit, buy, sell = max_profit(prices)

print("Maximum Profit:", profit)
print("Buy Day:", buy + 1)
print("Buy Price:", prices[buy])
print("Sell Day:", sell + 1)
print("Sell Price:", prices[sell])
