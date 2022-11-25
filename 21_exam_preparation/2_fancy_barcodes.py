import re
number_of_barcodes = int(input())
pattern_barcode = r"(@#+)(?P<product>[A-Z][a-zA-Z0-9]{4,}[A-Z])@#"
pattern_product_group = r"\d"
for current_barcode in range(number_of_barcodes):
    barcode_is_valid = False
    text = input()
    matches = re.finditer(pattern_barcode, text)
    for match in matches:
        matches2 = re.finditer(pattern_product_group, text)
        product_group = ""
        for match2 in matches2:
            digit = match2.group()
            product_group += digit
        if product_group == "":
            barcode_is_valid = True
            print("Product group: 00")
        else:
            barcode_is_valid = True
            print(f"Product group: {product_group}")
    if not barcode_is_valid:
        print("Invalid barcode")
