countries = input().split(", ")
capitals = input().split(", ")
result = zip(countries, capitals)
for pair in result:
    print(f"{pair[0]} -> {pair[1]}")
