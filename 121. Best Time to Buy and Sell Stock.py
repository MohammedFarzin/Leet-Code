prices = [7,1,5,3,6,4]

max_cur, max_so_far = 0, 0

for i in range(1, len(prices)):
    max_cur = max(0, max_cur + prices[i] - prices[i-1])
    max_so_far = max(max_so_far, max_cur)
print(max_so_far)