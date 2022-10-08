people_to_be_executed = input().split()
step = int(input())
people_left = len(people_to_be_executed)
list_of_order_of_executions = []
for execution in range(len(people_to_be_executed)):
    if step > len(people_to_be_executed):
        current_step = step - len(people_to_be_executed)
        while current_step > len(people_to_be_executed):
            current_step -= len(people_to_be_executed)
    else:
        current_step = step

    list_of_order_of_executions.append(int(people_to_be_executed[current_step - 1]))
    people_to_be_executed = people_to_be_executed[current_step:] + people_to_be_executed[: current_step - 1]
    people_left = len(people_to_be_executed)

final_print = ""
for printing in list_of_order_of_executions:
    final_print += str(printing)
    final_print += ","
final_print = final_print[0: -1]

print(f'[{final_print}]')
