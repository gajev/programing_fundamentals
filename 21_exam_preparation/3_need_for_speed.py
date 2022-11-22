number_of_cars = int(input())
cars = {}
for current_car in range(number_of_cars):
    car_to_add, start_mileage, start_fuel = input().split("|")
    cars[car_to_add] = [int(start_mileage), int(start_fuel)]
command = input()
while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    car = command[1]
    if action == "Drive":
        distance = int(command[2])
        drive_fuel = int(command[3])
        if drive_fuel > cars[car][1]:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= drive_fuel
            print(f"{car} driven for {distance} kilometers. {drive_fuel} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                cars.pop(car)
    elif action == "Refuel":
        refuel_fuel = int(command[2])
        if cars[car][1] + refuel_fuel > 75:
            added_fuel = 75 - cars[car][1]
            cars[car][1] = 75
            print(f"{car} refueled with {added_fuel} liters")
        else:
            cars[car][1] += refuel_fuel
            print(f"{car} refueled with {refuel_fuel} liters")
    elif action == "Revert":
        kilometers = int(command[2])
        cars[car][0] -= kilometers
        if cars[car][0] > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car][0] = 10000
    command = input()
for car, attributes in cars.items():
    print(f"{car} -> Mileage: {attributes[0]} kms, Fuel in the tank: {attributes[1]} lt.")
