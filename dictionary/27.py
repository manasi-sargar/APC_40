products={"Pen":20,"Book":5,"Bag":15,"Pencil":8}
products["Bottle"]=12
products["Pen"]=25
del products["Bag"]
name=input("Enter product to search: ")
if name in products:
    print("Product found:",products[name])
else:
    print("Product not found")
print("Products with quantity below 10:")
for product,quantity in products.items():
    if quantity<10:
        print(product,quantity)