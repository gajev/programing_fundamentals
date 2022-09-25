word = input()
list = []
index = 0
for capital in word:

    if capital.isupper():
        list.append(index)
    index += 1

print(list)
