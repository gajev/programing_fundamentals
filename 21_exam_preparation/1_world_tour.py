initial_stops = input()
command = input()
while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        new_string = command[2]
        if 0 <= index < len(initial_stops):
            initial_stops = initial_stops[:index] + new_string + initial_stops[index:]
        print(initial_stops)
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(initial_stops) and 0 <= end_index < len(initial_stops):
            initial_stops = initial_stops[:start_index] + initial_stops[end_index + 1:]
        print(initial_stops)
    elif action == "Switch":
        old_string = command[1]
        switch_string = command[2]
        if old_string in initial_stops:
            initial_stops = initial_stops.replace(old_string, switch_string)
        print(initial_stops)
    command = input()
print(f"Ready for world tour! Planned stops: {initial_stops}")
