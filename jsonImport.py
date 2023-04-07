import json

with open('friendJson.txt','r') as file:
    jsonContent=json.load(file)

print(jsonContent['friends'][0]['name'])

cars=[
    {'name':'ford','year':1995},
    {'name':'bmw','year':2001},
]

file=open('carsJson.txt','w')
json.dump(cars,file)
file.close()


myCarString='{"name":"fiat","model":2021}'
mycar=json.loads(myCarString)
print(mycar['name'])