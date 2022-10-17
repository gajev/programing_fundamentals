from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def distance(first, second, third, fourth):
    line_distance = first + second + third + fourth
    return line_distance


line_1 = distance(abs(x1), abs(y1), abs(x2), abs(y2))
line_2 = distance(abs(x3), abs(y3), abs(x4), abs(y4))
list_line_1 = [abs(x1), abs(y1), abs(x2), abs(y2)]
list_line_2 = [abs(x3), abs(y3), abs(x4), abs(y4)]
if line_1 >= line_2:
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
if line_1 < line_2:
    if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
        print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
    else:
        print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')



