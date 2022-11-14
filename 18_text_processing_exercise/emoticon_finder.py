text = input()
for index, symbol in enumerate(text):
    if symbol == ":":
        print(f':{text[index + 1]}')
