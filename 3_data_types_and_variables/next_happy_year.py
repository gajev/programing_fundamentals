current_year = int(input())
is_happy_year = False

while not is_happy_year:
    current_year += 1
    str_year = str(current_year)
    set_year = set()
    for digit in range(len(str_year)):
        set_year.add(str_year[digit])
    if len(str_year) == len(set_year):
        is_happy_year = True
print(current_year)

