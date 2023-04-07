readingFile=open('data.txt','r')
data=readingFile.read()
print(data)
readingFile.close()

writingFile=open('data.txt','w')
writingFile.write("Taha")
writingFile.close()

import utils.fileOperations

print(utils.fileOperations.readFile('data.txt'))

from utils.fileOperations import writeFile,readFile
writeFile('data.txt','ELMADAH')
print(readFile('data.txt'))