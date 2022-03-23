import json

f = open('/Users/bakhodirulugov/Desktop/webserver/countries.json')
   
data = json.load(f)

keys=['cym','deu','fra','hrv','ita','jpn','nld','por','rus','spa']

key = input('Enter the key:')

def translate(key):
    if key not in keys:
        print('Key is not supported!')
    elif key==None:
        print('Parameter cannot be empty!')
    else:
        for i in range(len(data)):
          print(data[i]['translations'][key])
    
    
translate(key)


f.close()