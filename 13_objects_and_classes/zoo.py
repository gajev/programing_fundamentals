class Zoo:
    __animals = []

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals.append(name)


    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {len(self.__animals)}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())
for current_animal in range(1, number_of_animals + 1):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

species_to_be_printed = input()
print(zoo.get_info(species_to_be_printed))


