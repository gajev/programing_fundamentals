number_of_letters = int(input())

printing_string = ""

for first in range(number_of_letters):
    for second in range(number_of_letters):
        for third in range(number_of_letters):
            print(f'{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}')
