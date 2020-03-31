# level1.py


def run_room(text, options):
    for i in range(len(text)):
        print(text[i])

    for k, v in options.items():
        print("[" + str(k) + "] " + v)

    val = input("Select the number of your choice ")
    return int(val)

    

def nest():
    room_text = ["A nest with a large egg sits in the middle", "It seems to be rocking slightly and warm"]

    options = {1: "Sit on the egg", 2: "Crush the egg", 3: "Go to the next room"}
    return run_room(room_text, options)

def dragon_lair():
    room_text = ["A large dragon is asleep and snoring softly", "There is treasure all around the dragon."]

    options = {1: "Cut off the dragon's head", 2: "Pet the dragon", 3: "Steal treasure"}
    return run_room(room_text, options)
    

