import re
initial_string = input()
destinations_list = []
travel_points = 0
pattern = r"(?P<symbol>=|\/)(?P<destination>[A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, initial_string)
for match in matches:
    destination = match.group("destination")
    destinations_list.append(destination)
for current_destination in destinations_list:
    travel_points += len(current_destination)
print(f"Destinations: {', '.join(destinations_list)}")
print(f"Travel Points: {travel_points}")
