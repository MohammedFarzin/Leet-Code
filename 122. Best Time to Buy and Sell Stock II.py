def max_profict(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])
    return profit

prices = [1,7, 5, 3, 6, 4]

max_profit = max_profict(prices)

print(max_profit)