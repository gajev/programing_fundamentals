def odd_and_even(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for current_digit in number:
        if int(current_digit) % 2 == 0:
            sum_of_even_digits += int(current_digit)
        else:
            sum_of_odd_digits += int(current_digit)
    return sum_of_odd_digits, sum_of_even_digits


number_as_string = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even(number_as_string)
print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')