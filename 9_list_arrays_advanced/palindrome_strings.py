initial_string = input().split()
palindrome = input()
final_list = []
palindrome_counter = 0
for current_string in initial_string:
    if current_string == current_string[::-1]:
        final_list.append(current_string)
    if current_string == palindrome:
        palindrome_counter += 1
print(final_list)
print(f"Found palindrome {palindrome_counter} times")