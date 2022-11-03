first_sequence = input().split(", ")
seconds_sequence = input().split(", ")
final_list = []
for i in first_sequence:
    for j in seconds_sequence:
        if i in j:
            if i in final_list:
                continue
            else:
                final_list.append(i)
print(final_list)
