#sets <<<<<<<<<<<<<<
student={1,2,3,4,5,6,7,4,9}
print("this is my first set:-", student)
print("type of my set:-",type(student))
print("length of my set:-",len(student ))
#dicard funx is used for removing element prsent in set or not peresnt in set.
#remove funx it is show erroe when the element will not present into a set .
student.discard(1)
print(student)
student.remove("2")
print(student)