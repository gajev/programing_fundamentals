initial_numbers = input().split()
numbers_for_print = []
for current_number in initial_numbers:
    numbers_for_print.append(abs(float(current_number)))
print(numbers_for_print)