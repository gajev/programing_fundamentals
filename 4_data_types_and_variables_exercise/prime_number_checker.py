number = int(input())
prime = True

for check in range(2, number):
    if number % check == 0:
        prime = False
print(prime)