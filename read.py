file=open('test.txt')
#print(file.read())#read all contents of test file
#print(file.read(7))#read sepecfic charater
#print(file.readline()) #read one full line
#print(file.readline())
#print(file.readline())

#line=file.readline()
#while(line!=''):
 #   print(line)
  #  line=file.readline()

for line in file.readlines():
    print(line)




