initial_string = input()
list_vowels = ["a", "o", "u", "e", "i"]
final_string = [letter for letter in initial_string if letter not in list_vowels]
print("".join(final_string))