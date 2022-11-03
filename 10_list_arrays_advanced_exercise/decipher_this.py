secret_message = input().split()

for index, current_word in enumerate(secret_message):
    first_letter_int = ""
    rest_part = ""
    for symbol in current_word:
        if symbol.isdigit():
            first_letter_int += symbol
        else:
            rest_part += symbol
    current_word = (chr(int(first_letter_int))) + rest_part
    secret_message[index] = current_word
    current_word = [word for word in current_word]
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    current_word = ''.join(current_word)
    secret_message[index] = current_word

print(*secret_message)





