from math import factorial
first_number = int(input())
second_number = int(input())
first_number_fact = factorial(first_number)
second_number_fact = factorial(second_number)
print(f"{first_number_fact / second_number_fact:.2f}")