#dicitonary:-- not allow the similar string or values.
#student={"name":"HARSH",
#"roll_number":15,
#"branch":"CSE",
#"year ":"second",
#"address":"jaipur"}
# name,class,roll_number,branch,address<<<<<<<<<<< keys.
#harsh second year, 21years old,cse,jaipur<<<<<<<<values
#keys+values="items"
#print("dicitonary:-",student)
#print("dict. keys:-",student.keys())
#print("dict. values:-",student.values())
#print("dict items:-",student.items())
#print(student['name'])
#print(student['branch'])
#print(student['address'])

#add item in python dict
#student['subject']='python language'
#print(student)
# task1:update functions , from keys 
#print(student.get('name')) #using to acess any keys.



#student={"name":"HARSH",
#"roll_number":15,
#"branch":"CSE",
#"year ":"second",
#"address":"jaipur"}

#student.clear() #this function is used for clear the dictionary function.
#student.copy() # this function is used for copy any keys in dictionary.
#student.pop()  # this function is used for adding any keys in the dictionary.
#student.push()# this function is used for deleting last will be adding into the dictionary.

#x=student.setdefault("color","white")
#print(x)

#task2 deep copy and shallow copy in python language.
#car={
  #  "brand":["ford","honda"],
 #"model":"mustang",
 #"year":1964
 #}
#print(car)

#car['year']=200
#print(car)

car={
    "brand":["ford","honda"],
 "model":"mustang",
 "year":1964
 }
for x in car.items():
    print(x)
for x in car.keys():
    print(x)
for x in car.values():
    print(x)
