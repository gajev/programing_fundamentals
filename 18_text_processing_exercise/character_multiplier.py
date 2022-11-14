first_string, second_string = input().split()
difference = abs(len(first_string) - len(second_string))
final_sum = 0
if len(first_string) >= len(second_string):
    for index in range(0, len(first_string) - difference):
        final_sum += ord(first_string[index]) * ord(second_string[index])
    for index_rest in range(len(first_string) - difference, len(first_string)):
        final_sum += ord(first_string[index_rest])
else:
    for index in range(0, len(second_string) - difference):
        final_sum += ord(second_string[index]) * ord(first_string[index])
    for index_rest in range(len(second_string) - difference, len(second_string)):
        final_sum += ord(second_string[index_rest])
print(final_sum)


