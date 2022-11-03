numbers = input().split(", ")
numbers = [int(i) for i in numbers]

for current_10 in range(1, 11):
    current_group = [number for number in numbers if number <= current_10 * 10]
    numbers = [number for number in numbers if number not in current_group]
    print(f"Group of {current_10}0's: {current_group}")
    if len(numbers) == 0:
        break
