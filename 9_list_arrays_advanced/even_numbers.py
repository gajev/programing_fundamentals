numbers_list = input().split(", ")
numbers_list = list(map(int, numbers_list))
index_list = [index for index in range(len(numbers_list)) if numbers_list[index] % 2 == 0]
print(index_list)