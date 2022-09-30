initial_numbers = input().split()
count_of_numbers_to_remove = int(input())
print(initial_numbers)
initial_numbers = [int(i) for i in initial_numbers]
print(initial_numbers)

for current_number in range(count_of_numbers_to_remove):
    smallest = min(initial_numbers)
    initial_numbers.remove(smallest)
print(*initial_numbers, sep=", ")
