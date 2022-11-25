import re
text = input()
countries_list = []
travel_points = 0

pattern = r"(=|\/)(?P<country>[A-Z][a-zA-Z][a-zA-Z]+)\1"
matches = re.finditer(pattern, text)
for match in matches:
    country = match.group("country")
    countries_list.append(country)
for points in countries_list:
    travel_points += len(points)
print(f"Destinations: {', '.join(countries_list)}")
print(f"Travel Points: {travel_points}")
