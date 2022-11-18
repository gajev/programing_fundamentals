command = input()
exam_pass_dictionary = {}
contestants_dictionary = {}
while True:
    if command == "end of contests":
        break
    command = command.split(":")
    exam_pass_dictionary[command[0]] = command[1]
    command = input()

new_command = input()
while True:
    if new_command == "end of submissions":
        break
    new_command = new_command.split("=>")
    contest = new_command[0]
    password = new_command[1]
    username = new_command[2]
    points = int(new_command[3])
    if contest in exam_pass_dictionary.keys():
        if password == exam_pass_dictionary[contest]:
            if username not in contestants_dictionary:
                contestants_dictionary[username] = [{contest: points}]
            else:
                exam_already_passed = False
                for taken_exam in contestants_dictionary[username]:
                    if contest in taken_exam:
                        exam_already_passed = True
                        if points > taken_exam[contest]:
                            taken_exam[contest] = points
                if not exam_already_passed:
                    contestants_dictionary[username].append({contest: points})
    new_command = input()
winner = ""
winner_points = 0
for current_student, current_score in contestants_dictionary.items():
    current_student_score = 0
    for dictionary in current_score:
        for score in dictionary.values():
            current_student_score += int(score)
    if current_student_score > winner_points:
        winner_points = current_student_score
        winner = current_student
print(f"Best candidate is {winner} with total {winner_points} points.")
print("Ranking:")

sorted_dict = {key: value for key, value in sorted(contestants_dictionary.items())}
for name, dict_courses in sorted_dict.items():
    print(name)
    list_for_printing = []
    for dict2 in dict_courses:
        dict_in_list = []
        for key2, value2 in dict2.items():
            dict_in_list.append(key2)
            dict_in_list.append(value2)
        list_for_printing.append(dict_in_list)
    final_list = sorted(list_for_printing, key=lambda item: item[-1], reverse=True)
    for printing in final_list:
        print(f"#  {printing[0]} -> {printing[1]}")

