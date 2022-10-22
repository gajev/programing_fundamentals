employee_happiness = input().split()
factor = int(input())
employee_happiness = [int(i) * factor for i in employee_happiness]
all_happiness = int(sum(current_number for current_number in employee_happiness))
average_happiness = all_happiness / len(employee_happiness)
counter = 0
for happy in employee_happiness:
    if happy >= average_happiness:
        counter += 1
if counter >= len(employee_happiness) * 0.5:
    print(f"Score: {counter}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(employee_happiness)}. Employees are not happy!")



