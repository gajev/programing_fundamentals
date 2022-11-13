initial_words = input().split()
for current_string in initial_words:
    print(current_string * len(current_string), end="")