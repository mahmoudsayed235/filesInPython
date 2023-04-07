csvFile=open('csvData.txt','r')
lines=csvFile.readlines()
csvFile.close()
lines=[line.strip() for line in lines[1:]]
for line in lines:
    personData=line.split(',')
    name=personData[0].title()
    age=personData[1]
    university=personData[2].title()
    degree=personData[3].capitalize()
    print(f'{name} is {age}, studing {degree} at {university}')