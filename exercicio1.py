products : list = [
    {
        "product_id" : "123",
        "product_name" : "milho",
        "validate_date" : "09-10-2024",
        "price" : 5
    },
    {
        "product_id" : "213",
        "product_name" : "garfo",
        "validate_date" : "20-10-2024",
        "price" : 15
    },
    {
        "product_id" : "777",
        "product_name" : "arroz",
        "validate_date" : "10-10-2024",
        "price" : 2
    }
]

prod_name = list()

for product in products:
    if product["price"] >= 5:
        print(f"{product["product_name"]} has the price above 5€")
        prod_name.append(product)

print(f"Output : {prod_name}")