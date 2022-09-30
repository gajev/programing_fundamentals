numbers = int(input())
positives = []
negatives = []
positives_counter = 0
negatives_counter = 0

for current_number in range(numbers):
    integer = int(input())
    if integer < 0:
        negatives.append(integer)
        negatives_counter += integer
    else:
        positives.append(integer)
        positives_counter += 1
print(positives)
print(negatives)
print(f'Count of positives: {positives_counter}')
print(f'Sum of negatives: {negatives_counter}')