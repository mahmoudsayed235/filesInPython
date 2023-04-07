readingFile=open('data.txt','r')
data=readingFile.read()
print(data)
readingFile.close()

writingFile=open('data.txt','w')
writingFile.write("Mahmoud")
writingFile.close()