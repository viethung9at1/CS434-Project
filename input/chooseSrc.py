f= open('./input/rockyou.txt', 'r')
i=100000
strToRead=list()
for i in range(0, i):
   strToRead.append(f.readline())
writeFile=open('./input/training.txt', 'w')
writeFile.writelines(strToRead)
