f= open('./input/rockyou.txt', 'r')
i=100000 # NUmber of lines in input
strToRead=list()
for i in range(0, i):
   strToRead.append(f.readline())
writeFile=open('./input/training.txt', 'w') 
writeFile.writelines(strToRead)
