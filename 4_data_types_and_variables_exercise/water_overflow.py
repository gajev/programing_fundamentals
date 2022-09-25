number_of_lines = int(input())
capacity = 255
liters_in_tank = 0

for liters in range (number_of_lines):
    entry = int(input())
    liters_in_tank += entry
    if capacity < liters_in_tank:
        liters_in_tank -= entry
        print("Insufficient capacity!")
print(liters_in_tank)