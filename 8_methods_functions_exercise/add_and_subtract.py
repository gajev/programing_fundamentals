def sum_of_numbers(first, second):
    return first_number + second_number


def subtract(sum, third):
    return sum - third_number


def add_and_subtract(first, second, third):
    sum_of_first_and_second = sum_of_numbers(first, second)
    result = subtract(sum_of_first_and_second, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))


