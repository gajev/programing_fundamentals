from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
sum_first_point = abs(x1) + abs(y1)
sum_second_point = abs(x2) + abs(y2)
if sum_first_point <= sum_second_point:
    print(f'({floor(x1)}, {floor(y1)})')
else:
    print(f'({floor(x2)}, {floor(y2)})')
