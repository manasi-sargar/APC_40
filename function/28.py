def subtotal(products):
    total = 0
    for price, quantity in products:
        total += price * quantity
    return total
def invoice(products):
    total = subtotal(products)
    discount = total * 0.10
    after_discount = total - discount
    gst = after_discount * 0.18
    return after_discount + gst
products = [
    (500, 2),
    (1000, 1)
]
print("Final Invoice =", invoice(products))