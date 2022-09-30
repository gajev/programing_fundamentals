initial_string = input().split()
length = len(initial_string)
middle_index = length // 2
first_half = initial_string[:middle_index]
second_half = initial_string[middle_index:]
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    last_shuffle = []
    for current_shuffle in range(middle_index):
        last_shuffle.append(first_half[0])
        first_half.remove(first_half[0])
        last_shuffle.append(second_half[0])
        second_half.remove(second_half[0])
    first_half = last_shuffle[:middle_index]
    second_half = last_shuffle[middle_index:]


print(last_shuffle)
