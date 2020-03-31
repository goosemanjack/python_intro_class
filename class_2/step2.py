name = input("Hello person. What is your name? ")
print("You are very smart, " + name)
print("Now that we know each other, what pronoun should I use when referring to you? ")

# mapped arrays
opts = [[1,2,3], ["He", "She", "They"]]

#if elif

print("Pick a value for your pronoun")
for i in range(len(opts[0])):
    print("[" + str(opts[0][i]) + "] " +  opts[1][i] )

proid = int(input("Value number? "))

pronoun = "not set"
if proid == 1:
    pronoun = "He"
elif proid == 2:
    pronoun = "She"
elif proid == 3:
    pronoun = "They"

# proid = int(input("Value number? ")) - 1
# pronoun = opts[1][proid]

print("Great. I just sent a message to my friend and said:")
print("Do you know " + name + "? " + pronoun + " is really cool!")

