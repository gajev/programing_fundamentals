initial_data = input().split()
odd_list = []
even_list = []
for current_number in initial_data:
    if int(current_number) % 2 != 0:
        odd_list.append(current_number)
    else:
        even_list.append(current_number)
command = 'Initial string'
while command != "end":
    command = command.split()
    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index + 1 > len(initial_data):
            print("Invalid index")
        else:
            initial_data = initial_data[index + 1:] + initial_data[:index + 1]
    elif command[0] == "max":
        if command[1] == "odd":
            if len(odd_list) == 0:
                print("No matches")
            else:
                max_odd = max(odd_list)
                last_index = 0
                for index, current_odd in enumerate(initial_data):
                    if current_odd == max_odd:
                        last_index = index
                print(last_index)
        elif command[1] == "even":
            if len(even_list) == 0:
                print("No matches")
            else:
                max_even = max(even_list)
                last_index = 0
                for index, current_even in enumerate(initial_data):
                    if current_even == max_even:
                        last_index = index
                print(last_index)
    elif command[0] == "min":
        if command[1] == "odd":
            if len(odd_list) == 0:
                print("No matches")
            else:
                min_odd = min(odd_list)
                last_index = 0
                for index, current_odd in enumerate(initial_data):
                    if current_odd == min_odd:
                        last_index = index
                print(last_index)
        elif command[1] == "even":
            if len(even_list) == 0:
                print("No matches")
            else:
                min_even = min(even_list)
                last_index = 0
                for index, current_even in enumerate(initial_data):
                    if current_even == min_even:
                        last_index = index
                print(last_index)
    elif command[0] == "first":
        if int(command[1]) > len(initial_data):
            print("Invalid count")
        else:
            odd_list2 = []
            even_list2 = []
            for current_number in initial_data:
                if int(current_number) % 2 != 0:
                    odd_list2.append(current_number)
                else:
                    even_list2.append(current_number)
            if command[2] == "odd":
                if len(odd_list2) < int(command[1]):
                    odd_list2 = ", ".join(odd_list2)
                    print(f"[{odd_list2}]")
                else:
                    index = int(command[1])
                    first_odd = odd_list2[: index]
                    first_odd = ", ".join(first_odd)
                    print(f"[{first_odd}]")
            elif command[2] == "even":
                if len(even_list2) < int(command[1]):
                    even_list2 = ", ".join(even_list2)
                    print(f"[{even_list2}]")
                else:
                    index = int(command[1])
                    first_even = even_list2[: index]
                    first_even = ", ".join(first_even)
                    print(f"[{first_even}]")
    elif command[0] == "last":
        if int(command[1]) > len(initial_data):
            print("Invalid count")
        else:
            odd_list2 = []
            even_list2 = []
            for current_number in initial_data:
                if int(current_number) % 2 != 0:
                    odd_list2.append(current_number)
                else:
                    even_list2.append(current_number)
            if command[2] == "odd":
                if len(odd_list2) < int(command[1]):
                    odd_list2 = ", ".join(odd_list2)
                    print(f"[{odd_list2}]")
                else:
                    index = int(command[1])
                    first_odd = odd_list2[index:]
                    first_odd = ", ".join(first_odd)
                    print(f"[{first_odd}]")
            elif command[2] == "even":
                if len(even_list2) < int(command[1]):
                    even_list2 = ", ".join(even_list2)
                    print(f"[{even_list2}]")
                else:
                    index = int(command[1])
                    first_even = even_list2[index:]
                    first_even = ", ".join(first_even)
                    print(f"[{first_even}]")

    command = input()
initial_data = ", ".join(initial_data)
print(f"[{initial_data}]")



