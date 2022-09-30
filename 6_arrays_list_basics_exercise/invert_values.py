list_of_numbers = input().split()
print(list_of_numbers)
opposite_numbers = []

for element in list_of_numbers:
    opposite_numbers.append(-int(element))
print(opposite_numbers)