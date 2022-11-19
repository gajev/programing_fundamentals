import re
number_of_strings = int(input())
pattern_name = r"@\b[A-Za-z]+|\b"
pattern_age = r'#\b[\d]+"*\b'
for sentence in range(number_of_strings):
    initial_string = input()
    matches_name = re.finditer(pattern_name, initial_string)
    matches_age = re.finditer(pattern_age, initial_string)
    for match in matches_name:
        if len(match.group()) > 0:
            name = match.group()[1:]
    for match in matches_age:
        if len(match.group()) > 0:
            age = match.group()[1:]
    print(f'{name} is {age} years old.')

