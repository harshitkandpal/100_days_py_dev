import random
names_string = input("Give names in the following format Rohit, Mohit, Soham")

# this string.split(", ") will the string wherever it finds the comma and space followed by it 
# hence crates a list of names.
names = names_string.split(", ")

# it will generate a random number between 0 and length of names -1 inclusively.
randomNumber = random.randint(0, len(names)-1)
print (names[randomNumber],"is going to pay the bill")


# another way to do this
# names_string = input("Give names in the following format Rohit, Mohit, Soham")
# names = names_string.split(", ")
# print (random.choice(names)+" is going to pay the bill")