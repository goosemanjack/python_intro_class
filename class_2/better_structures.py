
# mapped arrays
#opts = [[1,2,3], ["He", "She", "They"]]
opts = {1: "He", 2:"She", 3:"They"}

#if elif

print("Pick a value for your pronoun")

for key, val in opts.items():
    print("[" + str(key) + "] " + val )


# for i in range(len(opts[0])):
#     print("[" + str(opts[0][i]) + "] " +  opts[1][i] )

proid = int(input("Value number? "))

pronoun = opts.get(proid)

name = "John Doe"
print("Do you know " + name + "? " + pronoun + " is really cool!")




