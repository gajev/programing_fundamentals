initial_string = input().split()
characters = 'abcdefghijklmnopqrstuvwxyz'
dictionary = {}
for x in range(len(characters)):
    dictionary[characters[x]] = x+1
final_result = 0
for current_string in initial_string:
    first_letter = current_string[0]
    second_letter = current_string[-1]
    number = int(current_string[1:-1])
    result = 0
    if first_letter.isupper():
        lower_first = first_letter.lower()
        result = number / dictionary[lower_first]
    elif first_letter.islower():
        result = number * dictionary[first_letter]
    if second_letter.isupper():
        lower_second = second_letter.lower()
        result = result - dictionary[lower_second]
    elif second_letter.islower():
        result = result + dictionary[second_letter]
    final_result += result
print(f'{final_result:.2f}')




