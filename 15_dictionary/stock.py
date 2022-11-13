stock_list = input().split()
check_list = input().split()
stock_dictionary = {}
for index in range(0, len(stock_list), 2):
    key = stock_list[index]
    value = stock_list[index + 1]
    stock_dictionary[key] = int(value)
for check in check_list:
    if check in stock_dictionary:
        print(f"We have {stock_dictionary[check]} of {check} left")
    else:
        print(f"Sorry, we don't have {check}")