initial_numbers = input().split(", ")

for number in initial_numbers:
    palindrome = int((number)[::-1])
    if int(number) == palindrome:
        print("True")
    else:
        print("False")
