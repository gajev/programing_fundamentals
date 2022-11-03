list_products = input().split()
filtered_products = [print(product) for product in list_products if len(product) % 2 == 0]
