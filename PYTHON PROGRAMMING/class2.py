#TUPLE:--------
#tpl=(1,2,2,2,"hello",2.2,1.2)
#print("This my first tuple:",tpl)
#print("length of tuple:-",len(tpl))
#print("slicing:-",tpl[0-3])
#print("indexing:-",tpl[0])
#print("indexing:-",tpl[2])
#print("indexing:-",tpl[4])

#tuple unpacking
#a,b,c=(1,2,3)
#print(a)
#print(b)
#print(c)
tpl=(1,2,2,2,"hello",2.2,1.2)

print(tpl)
#print(tpl.count(1))
#(tpl.index(1))
#type casting
print("step1 coverting tuple into list")
print("Type of my tuple:-",type(tpl))#type of tuple
lst=list(tpl) # tuple covert into list
print(">>>>>>>>>>", lst) #print the list 
print("<<<<<<",type(lst)) #print list tuple 
lst.append(100) # adding any element in list 
print(lst)#print the list 
tpl=tuple(lst) #convert list into tuple final process 
print("final tuple:--",tpl)# print the final tuple 

