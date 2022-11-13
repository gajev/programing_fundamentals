command = input()
companies = {}
while True:
    if command == "End":
        break
    command = command.split(" -> ")
    company, employee_id = command[0], command[1]
    if company not in companies:
        companies[company] = [employee_id]
    else:
        if employee_id not in companies[company]:
            companies[company].append(employee_id)
    command = input()
for key, value in companies.items():
    print(key)
    for employee in value:
        print(f'-- {employee}')

