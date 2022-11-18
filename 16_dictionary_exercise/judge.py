
command = input()
dictionary_courses = {}
participants_dict = {}
while True:
    if command == "no more time":
        break
    command = command.split(" -> ")
    username = command[0]
    contest = command[1]
    points = int(command[2])
    if contest not in dictionary_courses.keys():
        dictionary_courses[contest] = [{username: points}]
        if username in participants_dict:
            participants_dict[username] += points
        else:
            participants_dict[username] = points
    else:
        is_user_participated = False
        for current_student_dict in dictionary_courses[contest]:
            if is_user_participated:
                break
            for current_student in current_student_dict:
                if username == current_student:
                    is_user_participated = True
                    break
            if is_user_participated:
                if points > current_student_dict[username]:
                    participants_dict[username] += points
                    participants_dict[username] -= current_student_dict[username]
                    current_student_dict[username] = points
                    break
        if not is_user_participated:
            dictionary_courses[contest].append({username: points})
            if username in participants_dict:
                participants_dict[username] += points
            else:
                participants_dict[username] = points
    command = input()
for course, participants in dictionary_courses.items():
    print(f'{course}: {len(participants)} participants')
    counter = 1
    list_dictionary_courses = []
    for dict2 in participants:
        student_list = []
        for key2, value2 in dict2.items():
            student_list.append(key2)
            student_list.append(value2)
        list_dictionary_courses.append(student_list)
    final_list = sorted(list_dictionary_courses, key=lambda item: (-item[1], item[0]))
    for printing in final_list:
        print(f'{counter}. {printing[0]} <::> {printing[1]}')
        counter += 1
print("Individual standings:")
final_list_ranking = []
for student_name, score in participants_dict.items():
    ranking_list = []
    ranking_list.append(student_name)
    ranking_list.append(score)
    final_list_ranking.append(ranking_list)
sorted_final_list_ranking = sorted(final_list_ranking, key=lambda item: (-item[1], item[0]))
counter2 = 1
for final_printing in sorted_final_list_ranking:
    print(f'{counter2}. {final_printing[0]} -> {final_printing[1]}')
    counter2 += 1
