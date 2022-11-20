raw_activation_key = input()
command = input()
while command != "Generate":
    command = command.split(">>>")
    operations = command[0]
    if operations == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif operations == "Flip":
        upper_lower, start_index, end_index = command[1], int(command[2]), int(command[3])
        if upper_lower == "Upper":
            raw_activation_key = raw_activation_key[:start_index] \
                + raw_activation_key[start_index: end_index].upper() + raw_activation_key[end_index:]
            print(raw_activation_key)
        elif upper_lower == "Lower":
            raw_activation_key = raw_activation_key[:start_index] \
                + raw_activation_key[start_index: end_index].lower() + raw_activation_key[end_index:]
            print(raw_activation_key)
    elif operations == "Slice":
        start_index, end_index = int(command[1]), int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
    command = input()
print(f"Your activation key is: {raw_activation_key}")







