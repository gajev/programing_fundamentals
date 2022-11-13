word = input()
while True:
    if word == "end":
        break
    print(f'{word} = {word[::-1]}')
    word = input()

