import re
url_list = []
pattern = r"www\.[a-zA-Z0-9\-]+\.[a-zA-Z]+\b(\.[a-zA-Z0-9\-]+)?(\.[a-zA-Z0-9\-]+)?"
while True:
    initial_string = input()
    matches = re.finditer(pattern, initial_string)
    if initial_string == "":
        break
    for match in matches:
        url_list.append(match.group())
for url in url_list:
    print(url)
