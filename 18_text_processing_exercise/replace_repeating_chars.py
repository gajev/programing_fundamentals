text = input()
final_output = text[0]
for character in text:
    if not character == final_output[-1]:
        final_output += character
print(final_output)