number_of_people = int(input())
current_state = input().split()
current_state = [int(i) for i in current_state]
free_spaces = 0
for spaces in current_state:
    if spaces == 0:
        free_spaces += 4
    elif spaces == 1:
        free_spaces += 3
    elif spaces == 2:
        free_spaces += 2
    elif spaces == 3:
        free_spaces += 1
while free_spaces > 0 and number_of_people != 0:
    for index, lifting in enumerate(current_state):
        people_to_take_lift = 4 - lifting
        if people_to_take_lift > number_of_people:
            lifting += number_of_people
            current_state[index] = lifting
            number_of_people = 0
            break
        if people_to_take_lift == 0:
            continue
        else:
            number_of_people -= people_to_take_lift
            free_spaces -= people_to_take_lift
            lifting += people_to_take_lift
            current_state[index] = lifting
if number_of_people == 0 and free_spaces > 0:
    print("The lift has empty spots!")
    print(*current_state)
elif number_of_people == 0 and free_spaces == 0:
    print(*current_state)
else:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
    print(*current_state)
