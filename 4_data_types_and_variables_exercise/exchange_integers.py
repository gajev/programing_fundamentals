a = int(input())
b = int(input())

old_a = a

print("Before:")
print(f'a = {a}')
print(f'b = {b}')
a = b
print("After:")
print(f'a = {a}')
print(f'b = {old_a}')