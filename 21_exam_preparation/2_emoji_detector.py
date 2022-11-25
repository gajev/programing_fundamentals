import re
text = input()
emoticon_list = []
emoticon_dict = {}
cool_threshold = 1
pattern = r"((\*\*)|::)(?P<emoticon>[A-Z][a-z][a-z]+)\1"
cool_pattern = r"(?P<number>\d)"
matches = re.finditer(pattern, text)
for match in matches:
    emoticon = match.group("emoticon")
    emoticon_list.append(emoticon)
matches = re.finditer(cool_pattern, text)
for match in matches:
    number = match.group("number")
    cool_threshold *= int(number)
for current_emoji in emoticon_list:
    coolness = 0
    for current_letter in current_emoji:
        coolness += ord(current_letter)
    emoticon_dict[current_emoji] = coolness
print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoticon_list)} emojis found in the text. The cool ones are:")
for key_emoji, value_emoji in emoticon_dict.items():
    if value_emoji > cool_threshold:
        if f"**{key_emoji}**" in text:
            print(f"**{key_emoji}**")
        elif f"::{key_emoji}::" in text:
            print(f"::{key_emoji}::")
