number_of_rooms = int(input())
enough_space = True
free_chairs_counter = 0
for current_room in range(1, number_of_rooms + 1):
    chairs_visitor = input().split()
    chairs = len(chairs_visitor[0])
    visitors = int(chairs_visitor[1])
    difference = visitors - chairs
    if visitors > chairs:
        print(f'{difference} more chairs needed in room {current_room}')
        enough_space = False
    else:
        free_chairs_counter += abs(difference)
if enough_space:
    print(f"Game On, {free_chairs_counter} free chairs left")

