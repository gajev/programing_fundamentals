number = int(input())
list_of_digits = []

for current_digit in range(len(str(number))):
    digit = number % 10
    list_of_digits.append(digit)
    number = int(number // 10)

list_of_digits.sort(reverse=True)

print(*list_of_digits, sep="")









