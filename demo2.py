#data types in python
str1='string datatype'
str2="string datatype with double quotes"

print(str1+ "concatinated" +str2)

a=2
b= 3.5
print(a)
print("{} {}" .format(a, str1))

#list datatype

values=[2, 3.4, "sand", 5]
print(values[0])
print(values)
print(values[2])
print(values[1])
print(values[1:2])
print(values[-1])
values.insert(3, 'mad')
print(values)

values.append("last")
values[2] = "bhrithi"
del values[1]
print(values)

#tuple data type
val=(2, 5.6, "chikku")
print(val[1])
print (val[2])
#val.insert(2,mad)
print(val)

#dictionary datatype

bal={1:"mad", "sand":3, "mom":"dad"}
print(bal[1])
print(bal["sand"])
print(bal["mom"])

#load dictionary in runtime

dic={}
dic["firstname"]= "sandhya"
dic["lastname"]= "muthappa"
print(dic["firstname"])
print(dic)