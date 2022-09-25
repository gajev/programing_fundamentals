key = int(input())
number_of_lines = int(input())
ascii_table = ""
for letter in range(number_of_lines):
    current_letter = input()
    ascii_value = ord(current_letter) + key
    ascii_table += chr(ascii_value)

print(ascii_table)