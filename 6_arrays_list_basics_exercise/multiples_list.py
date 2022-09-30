factor = int(input())
count = int(input())
list_of_numbers = []
last_factor = 0

for number in range(count):
    last_factor += factor
    list_of_numbers.append(last_factor)

print(list_of_numbers)