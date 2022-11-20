all_stops = input()
command = input()
while command != "Travel":
    command = command.split(":")
    manipulation = command[0]
    if manipulation == "Add Stop":
        index = int(command[1])
        city = command[2]
        if 0 <= index < len(all_stops):
            all_stops = all_stops[:index] + city + all_stops[index:]
            print(all_stops)
        else:
            print(all_stops)
    elif manipulation == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(all_stops) and 0 <= end_index < len(all_stops):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
            print(all_stops)
        else:
            print(all_stops)
    elif manipulation == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
            print(all_stops)
        else:
            print(all_stops)
    command = input()
print(f"Ready for world tour! Planned stops: {all_stops}")

