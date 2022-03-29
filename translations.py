import json
import os
import sys
from sys import argv


# Check if the command line has arguments, and if yes,
# assign the argument to the variable for main func, otherwise print error
if len(sys.argv) == 1:
    print("Parameter cannot be empty!")
    sys.exit()
else:
    key = argv[1]

# Making the script portable by defining absolute path
absolutePath = os.path.abspath("countries.json")

# Unpacking the .json file from absolute path defined above
f = open(absolutePath)

# Define a variable with data from the .json file
data = json.load(f)

# Define a dynamic list with supported translation keys
keys = []

# Dynamically add keys from the .json file to the list defined above
for i in data[0]["translations"]:
    keys.append(i)


# Main function that uses if-else statement to error-check and if none is triggered, translates country names
def translate(key):
    if key not in keys:
        print("Key is not supported!")
    else:
        for i in range(len(data)):
            print(data[i]["translations"][key])


# Call the main function
translate(key)

f.close()


