words = input().split()
words = list(map(lambda x: x.lower(), words))
final_dictionary = {}
odd_dictionary = {}
for word in words:
    if word not in final_dictionary:
        final_dictionary[word] = 1
    else:
        final_dictionary[word] += 1
for key, value in final_dictionary.items():
    if value % 2 != 0:
        odd_dictionary[key] = value
odd_list = odd_dictionary.keys()
print(*odd_list)