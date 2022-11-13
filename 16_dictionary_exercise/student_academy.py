number_of_pairs = int(input())
students_dictionary = {}

for records in range(number_of_pairs):
    student = input()
    current_grade = float(input())
    if student not in students_dictionary:
        students_dictionary[student] = [current_grade]
    else:
        students_dictionary[student].append(current_grade)
for key in students_dictionary.keys():
    total_grades = 0
    for sum_grades in students_dictionary[key]:
        total_grades += sum_grades
    average_grade = total_grades / len(students_dictionary[key])
    if average_grade >= 4.5:
        print(f"{key} -> {average_grade:.2f}")



