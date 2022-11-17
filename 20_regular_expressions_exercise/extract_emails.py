import re
initial_text = input()
pattern = r"^|(?<=\s)\b[a-zA-Z]+[\.\-\_]?[a-zA-Z0-9]+@[a-zA-Z]+([\-\_][a-zA-Z]+)?\.[a-zA-Z]+(\.[a-zA-Z]+)?\b"
matches = re.finditer(pattern, initial_text)
for match in matches:
    print(match.group())