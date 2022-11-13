command = input()
courses = {}
while True:
    if command == "end":
        break
    command = command.split(" : ")
    course, student = command[0], [command[1]]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
    command = input()
for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for name in value:
        for student_name in name:
            print(f"-- {student_name}")

