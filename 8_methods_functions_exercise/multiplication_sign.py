first_number = int(input())
second_number = int(input())
third_number = int(input())
zero = False
negative_counter = 0

list_numbers = [first_number, second_number, third_number]
for number in list_numbers:
    if number == 0:
        zero = True
        break
    elif number < 0:
        negative_counter += 1
if zero:
    print("zero")
elif negative_counter == 1 or negative_counter == 3:
    print("negative")
else:
    print("positive")