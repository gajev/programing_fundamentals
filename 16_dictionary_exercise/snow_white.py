name_hat_color_physics = input()
dwarfs = {}
while name_hat_color_physics != "Once upon a time":
    name_hat_color_physics = name_hat_color_physics.split(" <:> ")
    dwarf_name = name_hat_color_physics[0]
    hat_color = name_hat_color_physics[1]
    dwarf_physics = int(name_hat_color_physics[2])
    dwarfs[hat_color] = dwarfs.get(hat_color, {})
    dwarfs[hat_color][dwarf_name] = dwarfs[hat_color].get(dwarf_name, dwarf_physics)
    if dwarfs[hat_color][dwarf_name] < dwarf_physics:
        dwarfs[hat_color][dwarf_name] = dwarf_physics

    name_hat_color_physics = input()
list_all_dwarfs = []
for hat in dwarfs:
    for key, value in dwarfs[hat].items():
        list_all_dwarfs.append({"colors": len(dwarfs[hat]), "name": key, "physics": value, "hat_color": hat})
for final_print in sorted(list_all_dwarfs, key=lambda x: (-x["physics"], -x["colors"])):
    print(f"({final_print['hat_color']}) {final_print['name']} <-> {final_print['physics']}")

