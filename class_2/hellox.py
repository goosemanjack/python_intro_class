
def main_func():
    name = input("What is your name? ")
    print("Hello, " + name)

    opts = [[1,2,3,4,5,6], ["He", "She", "They", "Doggy", "Froggy", "Dragon"]]

    # theyVal = opts[1][2]
    print("Choose a pronoun by using the number from the list below")

    for i in range(len(opts[0])):
        print("[" + str(opts[0][i]) + "] " + opts[1][i])

    pnum = input("Make your selection: ")

    pnum = int(pnum)-1

    pronoun = opts[1][pnum]
    print("You like " + pronoun)
    ask_flowers(pronoun)


def ask_flowers(pnoun):
    print("Since you like " + pnoun + " as your pronoun, maybe you like flowers")
    ans = input("do you like flowers? yes or no ")
    if ans == "yes":
        print("here is a pretty flower ")
        print(ascii_flower())
    else:
        print("too bad")


def ascii_flower():
    f = '''
	  /-_-\\
	 /  /  \\
	/  /    \\
	\  \    /
	 \__\__/
	    \\
	    -\\    ____
	      \\  /   /
	____   \\/___/
	\   \ -//
	 \___\//-
	    -//
	     \\
	     //
	    //-
	  -//
	  //
	  \\
	   \\'''

    return f

# Entry point to start the program
main_func()
