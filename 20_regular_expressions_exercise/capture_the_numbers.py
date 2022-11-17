import re

pattern = r"\d+"
while True:
    initial_string = input()
    matches = re.finditer(pattern, initial_string)
    if initial_string == "":
        break
    for match in matches:
        print(match.group(), end=" ")
