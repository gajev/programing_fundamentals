initial_string = input()
digits, letters, other_symbols = [], [], []
for current_symbol in initial_string:
    if current_symbol.isdigit():
        digits.append(current_symbol)
    elif current_symbol.isalpha():
        letters.append(current_symbol)
    else:
        other_symbols.append(current_symbol)
print("".join(digits))
print("".join(letters))
print("".join(other_symbols))