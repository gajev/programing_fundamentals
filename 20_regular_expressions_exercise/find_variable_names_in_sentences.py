import re
text = input()
printing_list = []
pattern = r"\b_[a-zA-Z0-9]*\b"
matches = re.finditer(pattern, text)
for match in matches:
    printing_list.append(match.group())
for index in range(len(printing_list)):
    printing_list[index] = printing_list[index][1:]


print(",".join(printing_list))
