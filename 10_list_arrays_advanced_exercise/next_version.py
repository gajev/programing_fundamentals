current_version = input().split(".")
current_version = [int(i) for i in current_version]
current_version[-1] += 1
for index in range(len(current_version) - 1, -1, - 1):
    if current_version[index] == 10:
        current_version[index] = 0
        if index - 1 >= 0:
            current_version[index - 1] += 1
print(*current_version, sep=".")


