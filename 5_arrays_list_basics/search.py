number_of_words = int(input())
key_word = input()
list_of_words = []

for current_string in range (number_of_words):
    next_string = (input())
    list_of_words.append(next_string)
print(list_of_words)

changed_list = []

for current_word in list_of_words:
    if key_word in current_word:
        changed_list.append(current_word)
print(changed_list)