initial_courses = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    action = command[0]
    lesson = command[1]
    if action == "Add":
        if lesson not in initial_courses:
            initial_courses.append(lesson)
    elif action == "Insert":
        index = int(command[2])
        if lesson not in initial_courses:
            initial_courses.insert(index, lesson)
    elif action == "Remove":
        if lesson in initial_courses:
            index = initial_courses.index(lesson)
            initial_courses.remove(lesson)
            if index < len(initial_courses):
                if "Exercise" in initial_courses[index]:
                    initial_courses.remove(initial_courses[index])
    elif action == "Swap":
        swap_lesson = command[2]
        if lesson in initial_courses and swap_lesson in initial_courses:
            index1 = initial_courses.index(lesson)
            index2 = initial_courses.index(swap_lesson)
            first_has_exercise = False
            second_has_exercise = False
            if index1 + 1 < len(initial_courses):
                first_has_exercise = "Exercise" in initial_courses[index1 + 1]
            if index2 + 1 < len(initial_courses):
                second_has_exercise = "Exercise" in initial_courses[index2 + 1]
            initial_courses[index1], initial_courses[index2] = initial_courses[index2], initial_courses[index1]
            if first_has_exercise and second_has_exercise:
                initial_courses[index1 + 1], initial_courses[index2 + 1] \
                    = initial_courses[index2 + 1], initial_courses[index1 + 1]
            elif not first_has_exercise and second_has_exercise:
                initial_courses.insert(index1 + 1, initial_courses.pop(index2 + 1))
            elif first_has_exercise and not second_has_exercise:
                initial_courses.insert(index2 + 1, initial_courses.pop(index1 + 1))
    elif action == "Exercise":
        exercise = str(lesson + "-" + action)
        if lesson in initial_courses and exercise not in initial_courses:
            index = initial_courses.index(lesson)
            initial_courses.insert(index + 1, exercise)
        else:
            initial_courses.append(lesson)
            initial_courses.append(exercise)

    command = input()
for indexes, elements in enumerate(initial_courses):
    number = indexes + 1
    print(f'{number}.{elements}')
