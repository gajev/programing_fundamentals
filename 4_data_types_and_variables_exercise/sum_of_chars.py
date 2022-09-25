number_of_letters = int(input())

counter = 0

for letter in range(number_of_letters):
    current_letter = (input())
    counter += ord(current_letter)

print(f'The sum equals: {counter}')
