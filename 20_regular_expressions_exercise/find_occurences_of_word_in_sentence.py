import re
text = input().lower()
word = input().lower()
counter = 0
pattern = fr"\b{word}\b"
matches = re.finditer(pattern, text)
for match in matches:
    counter += 1
print(counter)