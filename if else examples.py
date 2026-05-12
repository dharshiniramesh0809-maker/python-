     >   greater than
     <   less than
     
score=int(input("score"))
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("averag student")
elif(score>70 and score<100):
    print("good student")
else:
    print("invalid input")



a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/div/mul:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("no values")




score=int(input("score"))
if(score>=70):
    location=input("your location:")
    department=input("your department:")
    print("eligeble")
else:
    print("not")
