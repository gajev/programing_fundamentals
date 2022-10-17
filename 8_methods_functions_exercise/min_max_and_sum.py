initial_data = input().split()
data_as_int = [int(item) for item in initial_data]
minimum_number = min(data_as_int)
maximum_number = max(data_as_int)
sum_numbers = sum(data_as_int)
print(f'The minimum number is {minimum_number}')
print(f'The maximum number is {maximum_number}')
print(f'The sum number is: {sum_numbers}')
