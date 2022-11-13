initial_string = input().split(":")
student_dictionary = {}
while len(initial_string) > 1:
    student_name, student_id, course = initial_string[0], initial_string[1], initial_string[2]
    if course not in student_dictionary:
        student_dictionary[course] = []
    student_dictionary[course].append(f'{student_name} - {student_id}')
    initial_string = input().split(":")
searched_course = initial_string[0].replace("_", " ")
for student in student_dictionary[searched_course]:
    print(student)


