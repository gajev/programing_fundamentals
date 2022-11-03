from math import ceil
number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
attendance = 0
if total_number_of_lectures == 0:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")
    quit()
max_bonus = attendance / total_number_of_lectures * (5 + additional_bonus)
for student in range(1, number_of_students + 1):
    current_attendance = int(input())
    current_bonus = ceil(current_attendance / total_number_of_lectures * (5 + additional_bonus))
    if current_bonus >= max_bonus:
        max_bonus = current_bonus
        if attendance <= current_attendance:
            attendance = current_attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendance} lectures.")
