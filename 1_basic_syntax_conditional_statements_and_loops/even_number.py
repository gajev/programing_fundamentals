n = int(input())

even_numbers = True

for i in range (n):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        even_numbers = False
        break
    else:
        continue

if even_numbers:
    print("All numbers are even.")