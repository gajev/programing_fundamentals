count_of_numbers = int(input())
list_numbers = [1, 1, 2]

for current_number in range(4, count_of_numbers + 1):
    next_number = list_numbers[current_number - 2] + list_numbers[current_number - 3] + list_numbers[current_number - 4]
    list_numbers.append(next_number)
if count_of_numbers == 2:
    list_numbers = [1, 1]
elif count_of_numbers == 1:
    list_numbers = [1]
elif count_of_numbers <= 0:
    list_numbers = []

print(*list_numbers)
