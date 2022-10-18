first_number_of_students = int(input())
second_number_of_students = int(input())
third_number_of_students = int(input())
student_count = int(input())
all_student_per_hours = first_number_of_students + second_number_of_students + third_number_of_students
hours_counter = 1
while student_count > all_student_per_hours:
    hours_counter += 1
    student_count -= all_student_per_hours
    if hours_counter % 4 == 0:
        hours_counter += 1
if student_count == 0:
    hours_counter = 0
print(f"Time needed: {hours_counter}h.")
