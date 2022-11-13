initial_input = input().split()
my_dictionary = {}
for current_word in initial_input:
    for current_letter in current_word:
        if current_letter not in my_dictionary:
            my_dictionary[current_letter] = 0
        my_dictionary[current_letter] += 1
for key, value in my_dictionary.items():
    print(f"{key} -> {value}")
