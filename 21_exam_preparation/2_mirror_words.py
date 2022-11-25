import re
text = input()
words = {}
mirror_words_dict = {}
mirror_words_list = []
pattern = r"(#|@)(?P<first_word>[a-zA-Z]{3,})\1{2}(?P<second_word>[a-zA-Z]{3,})\1"
matches = re.finditer(pattern, text)
for match in matches:
    word = match.group("first_word")
    word2 = match.group("second_word")
    words[word] = word2
if len(words) == 0:
    print("No word pairs found!")
else:
    print(f"{len(words)} word pairs found!")
for key, value in words.items():
    if key == value[::-1]:
        mirror_words_dict[key] = value
for first, second in mirror_words_dict.items():
    mirror_words_list.append(f"{first} <=> {second}")
if len(mirror_words_list) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words_list))


