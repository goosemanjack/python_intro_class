# level1.py


def first_room():
    print("Welcome to the dungeon. You walk into the first room and see an empty hall.")
    print("There is an ominous door at the far end of this hall.")
    options = {1: "Go back home to safety", 2: "Go through door"}

    for k, v in options.items():
        print("[" + str(k) + "] " + v)

    val = input("Select the number of your choice ")
    return int(val)


def second_room():
    print("A box stands in the middle of this room. There is a skull and crossbones on the box.")
    print("Do you open the box or ignore it and continue through the next door?")

    options = {1: "Open the box", 2: "Continue through the next door", 3: "Go back to entrance"}
    for k, v in options.items():
        print("[" + str(k) + "] " + v)

    val = input("Select the number of your choice ")
    return int(val)
    
def next_level():
    print("There are stairs leading down.")
    options = {1: "Go back home to safety", 2: "Descend the stairs"}

    for k, v in options.items():
        print("[" + str(k) + "] " + v)

    val = input("Select the number of your choice ")
    return int(val)


 