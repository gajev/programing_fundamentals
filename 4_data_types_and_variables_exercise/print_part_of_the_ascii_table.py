first_number = int(input())
last_number = int(input())

ascii_table = []
for character in range(first_number, last_number +1):
    ascii_table += chr(character)


print(*ascii_table)