number = int(input())
sum_of_digits = 0
for current_number in range (1, number):
    if number % current_number == 0:
        sum_of_digits += current_number
if sum_of_digits == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
