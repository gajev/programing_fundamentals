name = input()
voldermort = True

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        voldermort = False
        break
    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    else:
        print(f'{name} goes to Hufflepuff.')
    name = input()

if voldermort:
    print("Welcome to Hogwarts.")
