initial_vehicle = input().split(">>")
tax_collected = 0
for vehicle in initial_vehicle:
    vehicle = vehicle.split(" ")
    vehicle_type = vehicle[0]
    years = int(vehicle[1])
    kilometers = int(vehicle[2])
    initial_tax = 0
    if vehicle_type == "family":
        initial_tax = 50
        initial_tax -= 5 * years
        initial_tax += (kilometers // 3000) * 12
        tax_collected += initial_tax
        print(f"A {vehicle_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif vehicle_type == "heavyDuty":
        initial_tax = 80
        initial_tax -= 8 * years
        initial_tax += (kilometers // 9000) * 14
        tax_collected += initial_tax
        print(f"A {vehicle_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif vehicle_type == "sports":
        initial_tax = 100
        initial_tax -= 9 * years
        initial_tax += (kilometers // 2000) * 18
        tax_collected += initial_tax
        print(f"A {vehicle_type} car will pay {initial_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")
print(f"The National Revenue Agency will collect {tax_collected:.2f} euros in taxes.")
