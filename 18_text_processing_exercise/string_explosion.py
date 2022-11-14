text = input()
explosion = 0
final_text = ""
for index, symbol in enumerate(text):
    if symbol == ">":
        explosion += int(text[index + 1])
        final_text += ">"
        continue
    if explosion > 0:
        explosion -= 1
    else:
        final_text += symbol
print(final_text)

