"""Try reading the contents of animals.txt and from there create a
file named animals-sorted.txt that is sorted alphabetically."""

unsorted_animal_file = "animals.txt"
sorted_animal_file = "sorted-animals.txt"
animals = []


with open(unsorted_animal_file) as unsorted:
    for line in unsorted:
        animals.append(line)
    animals.sort()


print("The file {} cannot be opened.".format(unsorted_animal_file))


with open(sorted_animal_file, "w") as sorted:
    for animal in animals:
        sorted.write(animal)