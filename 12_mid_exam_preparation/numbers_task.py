numbers = input().split()
numbers = [int(i) for i in numbers]
sum_numbers = 0
last_list = []

for current_number in numbers:
    sum_numbers += current_number
average = sum_numbers / len(numbers)
for current_number in numbers:
    if current_number > average:
        last_list.append(current_number)
last_list.sort()
last_list.reverse()
if len(last_list) == 0:
    print("No")
elif len(last_list) <= 5:
    print(*last_list, sep=" ")
else:
    last_list = last_list[:5]
    print(*last_list, sep=" ")
