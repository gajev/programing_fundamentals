event = input()
cofee_counter = 0

while event != "END":

    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        cofee_counter += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        cofee_counter += 2
    else:
        pass
    event = input()

if cofee_counter > 5:
    print("You need extra sleep")
else:
    print(cofee_counter)




