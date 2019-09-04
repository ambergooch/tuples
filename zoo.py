zoo = ("tiger", "wolf", "kangaroo", "panda", "zebra", "lion", "dolphin", "otter", "seal", "platypus")

print(zoo.index("panda"))

animal_to_find = "alligator"
if animal_to_find in zoo:
    print("animal found")
else:
    print("animal not found")

(animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9, animal_10) = zoo
print(animal_1)
print(animal_4)
print(animal_6)
print(animal_10)

tuple_to_list = list(zoo)
tuple_to_list.extend(["stingray", "lynx"])
print(tuple_to_list)

list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)