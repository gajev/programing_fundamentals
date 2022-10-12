def rounding():
    last_list = []
    for current_number in initial_input:
        last_list.append(round(float(current_number)))
    return last_list

initial_input = input().split()
print(rounding())
