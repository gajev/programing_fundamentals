number_of_integers = int(input())

even = []
odd = []
positive = []
negative = []

for current_number in range(number_of_integers):
    number = int(input())
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)