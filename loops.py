#if condition
""""""
obj="say hello"
if obj== "say":
    print("condition wrong")
else:
    print("say hello")
print(" condition ended")

#for loops

a = [1,2,3,4,5]
for i in a:
    print (i+1)

for j in range(1,6):
    print(j*3)

for k in range (1,8,2):
    print (k)

add=0;
for m in range(0,9):
    add=add+m
print(add)

""""""
#swap

num1="sand"
num2="mad"
print(num1)
print(num2)
temp = num1
num1=num2
num2=temp
print(num1)
print(num2)


nume = 2
count=0
if nume>1:
    for i in range(1, nume+1):
        if nume%i==0:
            count=count+1
    if count==2:
        print("nume is prime")
    else:
        print("nume is not prime")


