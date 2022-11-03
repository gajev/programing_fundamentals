class Party:

    def __init__(self):
        self.people_names_list = []


party = Party()
name = input()
while name != "End":
    party.people_names_list.append(name)
    name = input()

print(f"Going: {', '.join(party.people_names_list)}")
print(f"Total: {len(party.people_names_list)}")