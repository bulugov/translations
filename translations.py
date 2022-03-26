import json


#Open the required file
f = open('/Users/bakhodirulugov/Desktop/webserver/countries.json')
 
#Assign a variable with data from .json file
data = json.load(f)

#Define the accepted keys for the function
keys=['cym','deu','fra','hrv','ita','jpn','nld','por','rus','spa']

#Ask the user for an input and assign it to the variable
key = input('Enter the key:')

#Translation function that takes user input as a parameter and checks if it fits the requirements in if-else statement
def translate(key):
    if key not in keys:
        print('Key is not supported!')
    elif key is None:
        print('Parameter cannot be empty!')
    else:
        for i in range(len(data)):
          print(data[i]['translations'][key])
    
    
translate(key)


f.close()
