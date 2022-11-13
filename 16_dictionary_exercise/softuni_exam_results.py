command = input()
student_dictionary = {}
language_dictionary = {}
submission_counter = 0
while command != "exam finished":
    result = command.split("-")
    if result[1] == "banned":
        if result[0] in student_dictionary:
            student_dictionary.pop(result[0])
        command = input()
        continue
    else:
        username = result[0]
        language = result[1]
        points = int(result[2])
        if language in language_dictionary:
            language_dictionary[language] += 1
        else:
            language_dictionary[language] = 1
        if username not in student_dictionary:
            student_dictionary[username] = [language, points]
        else:
            if language in student_dictionary[username]:
                if points > student_dictionary[username][1]:
                    student_dictionary[username][1] = points
    command = input()
print("Results:")
for key, value in student_dictionary.items():
    print(f"{key} | {value[-1]}")
print("Submissions:")
for key, value in language_dictionary.items():
    print(f"{key} - {value}")