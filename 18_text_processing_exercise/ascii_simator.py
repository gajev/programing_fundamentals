first_symbol = ord(input())
second_symbol = ord(input())
final_string = input()
sum_symbols = 0
for symbol in final_string:
    if first_symbol < ord(symbol) < second_symbol:
        sum_symbols += ord(symbol)
print(sum_symbols)
