banned_words = input().split(", ")
text = input()
for check in banned_words:
    while check in text:
        text = text.replace(check, "*" * len(check))
print(text)
