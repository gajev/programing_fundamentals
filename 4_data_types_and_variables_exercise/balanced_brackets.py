number_of_lines = int(input())
counter_opening_bracket = 0
counter_closing_bracket = 0

for current in range(number_of_lines):
    current_n = input()
    if current_n == '(':
        counter_opening_bracket += 1
    elif current_n == ')':
        counter_closing_bracket += 1
    if abs(counter_opening_bracket - counter_closing_bracket) != 1 and \
            abs(counter_opening_bracket - counter_closing_bracket) != 0:
        break
    if counter_closing_bracket > counter_opening_bracket:
        break

if counter_opening_bracket == counter_closing_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")
