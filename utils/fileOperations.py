def readFile(file):
    with open(file,'r')as file:
        return file.readlines()

def writeFile(file,context):
    with open(file,'w')as file:
        file.write(context)