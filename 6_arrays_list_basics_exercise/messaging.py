sequence_of_numbers = input().split()
string_input = input()
sum_digits_list = []
for digits in sequence_of_numbers:
    sum_digits = 0
    for digit in digits:
        sum_digits += int(digit)
    sum_digits_list.append(sum_digits)
final_word = ""
for letter in sum_digits_list:
    if letter < len(string_input):
        final_word += string_input[letter]
        index = int(letter)
        string_input = string_input[0: index:] + string_input[index + 1::]
    else:
        letter = letter - len(string_input)
        final_word += string_input[letter]
        index = int(letter)
        string_input = string_input[0: index:] + string_input[index + 1::]
print(final_word)