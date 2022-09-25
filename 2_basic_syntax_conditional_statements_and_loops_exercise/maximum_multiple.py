divisor = int(input())
boundary = int(input())
n = 0


for i in range(boundary, divisor, -1):
    if i % divisor == 0:
        n += i
        print(n)
        break

