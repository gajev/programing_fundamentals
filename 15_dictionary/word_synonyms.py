number = int(input())
dictionary = {}
for pair in range(number):
    key_word = input()
    value_word = input()
    if key_word not in dictionary:
        dictionary[key_word] = [value_word]
    else:
        dictionary[key_word].append(value_word)
for key, value in dictionary.items():
    print(f'{key} - {", ".join(value)}')
