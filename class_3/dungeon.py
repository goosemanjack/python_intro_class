# Dungeon Crawler

import asciiart
import level1
import level2
import time   # timer


#def test():
#    print(asciiart.baby_dragon())
#    print(asciiart.big_skull())
#    print(asciiart.dragon())
#    print(asciiart.samurai())
#    print(asciiart.skull_cross())
#    print(asciiart.warrior())
#    print(asciiart.chicken())


def start_dungeon():
    result = level1.first_room()

    if result == 1:
        print(asciiart.chicken())
        print("Have fun baking pies in safety, you baby.")
        return
    else:
        print("You are a brave soul!")
        print("")

    time.sleep(0.75)

    result = level1.second_room()

    if(result == 1):
        print(asciiart.skull_cross())
        print("You are dead. It should have been obvious not to open the box.")
        return
    elif(result == 3):
        return start_dungeon()
    
    print("")
    result = level1.next_level()

    if(result == 1):
        result = level1.second_room()
        #...
        return
    elif(result == 2):
        return run_second_room()



def run_second_room():
    print("")
    result = level2.nest()

    if result == 1:
        print(asciiart.baby_dragon())
        time.sleep(0.75)
        print("You have birthed a baby!")
        return
    elif result == 2:
        print(asciiart.dragon())
        print("Oh no! Momma dragon is here and she isn't happy!")
        time.sleep(1.25)
        print(asciiart.big_skull())
        print("You are dead")
        return
    
    print("")
    result = level2.dragon_lair()
    if result == 1:
        print(asciiart.samurai())
        time.sleep(1.1)
        print(asciiart.dragon())
        time.sleep(1.25)
        print("....")
        time.sleep(0.25)
        print("You are VICTORIOUS!!!")
        return
    else:
        print(asciiart.dragon())
        print("The dragon awakens! Prepare for battle.")
        time.sleep(0.75)
        print(asciiart.big_skull())
        print("You are dead")









start_dungeon()



