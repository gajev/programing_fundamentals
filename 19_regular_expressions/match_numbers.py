import re
initial_string = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, initial_string)
for match in matches:
    print(match.group(), end=" ")

