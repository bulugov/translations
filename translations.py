import json
import os
import sys


# Checking if the command line has arguments, and if yes,
# assign the argument to the variable for main func, otherwise print error
if len(sys.argv) == 1:
    print("Parameter cannot be empty!")
    sys.exit()
else:
    key = sys.argv[1]

# Making the script portable by defining absolute path
absolutePath = os.path.abspath("countries.json")

# Unpacking the .json file from absolute path defined above
f = open(absolutePath)

# Defining a variable with data from the .json file
data = json.load(f)

# Defining a dynamic global list for error-checking related with unsupported user input
keys = []

# Filling in the global list defined above
for i in range(len(data)):
    for j in data[i]["translations"]:
        if j not in keys:
            keys.append(j)


# Main function that uses if-else statement to error-check and if none is triggered, translates country names
def translate(key):
    if key not in keys:
        print("Key is not supported!")
    else:
        for i in range(len(data)):
            if key in data[i]["translations"]:
                print(data[i]["translations"][key]["official"])


# Call the main function
translate(key)

f.close()
