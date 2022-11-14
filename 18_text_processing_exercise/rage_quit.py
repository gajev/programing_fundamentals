initial_string = input()
unique_symbols = []
temp_string = ""
final_string = ""
number = 0
for index, current_symbol in enumerate(initial_string):
    if not current_symbol.isdigit():
        temp_string += current_symbol.upper()
        if current_symbol.lower() not in unique_symbols:
            unique_symbols.append(current_symbol.lower())
    else:
        if index + 1 < len(initial_string):
            if initial_string[index + 1].isdigit():
                number = 10 * int(initial_string[index]) + int(initial_string[index + 1])
                final_string += int(number) * temp_string
                temp_string = ""
            else:
                number = current_symbol
                final_string += int(number) * temp_string
                temp_string = ""
        else:
            number = current_symbol
            final_string += int(number) * temp_string
            temp_string = ""
print(f"Unique symbols used: {len(unique_symbols)}")
print(final_string)
