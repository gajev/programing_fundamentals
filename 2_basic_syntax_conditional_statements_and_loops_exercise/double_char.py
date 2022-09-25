command = input()


while command != "End":
    word = ""
    if command == "SoftUni":
        command = input()
        continue
    for current_letter in command:
        word = word + current_letter*2
        if len(word) == 2*len(command):
            print(word)
    command = input()