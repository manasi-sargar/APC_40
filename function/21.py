def total_bill(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    if total >= 5000:
        discount = total * 0.10
    else:
        discount = total * 0.05
    return total - discount
prices = [100, 200, 500]
quantities = [2, 3, 1]
print("Final Bill =", total_bill(prices, quantities))