list_of_integers = input().split(", ")
count_of_beggars = int(input())
final_list = []
index_counter = 0
list_of_integers_int = [int(i) for i in list_of_integers]


while count_of_beggars > index_counter:
    temp_sum = 0
    for element in range(index_counter, len(list_of_integers_int), count_of_beggars):
        temp_sum += list_of_integers_int[element]
    final_list.append(temp_sum)
    index_counter += 1
print(final_list)