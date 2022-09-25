n = int(input())

for i in range(1, n + 1):
    word = (input())
    if "," in word or "." in word or "_" in word:
        print(f'{word} is not pure!')
    else:
        print(f'{word} is pure.')

