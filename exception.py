itemincart=0
#if itemincart!=2:
   # raise Exception("product item counts are not matching")
#pass
#assert(itemincart==2)

try:
    with open('filename.txt') as reader:
        reader.read()
except Exception as e:
    print (e)
    #print("some how i reached this block coz try blocked failed")

finally:
    print("clear all resources")