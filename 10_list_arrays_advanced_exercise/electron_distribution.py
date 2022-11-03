number_of_electrons = int(input())
n = 1
maximum_number_of_electrons = 2 * n*n
current_electron = 0
list_electron = []
for shell in range(1, number_of_electrons + 1):
    current_electron += 1
    if current_electron == maximum_number_of_electrons:
        list_electron.append(current_electron)
        n += 1
        maximum_number_of_electrons = 2 * n * n
        current_electron = 0
if current_electron > 0:
    list_electron.append(current_electron)
print(list_electron)
