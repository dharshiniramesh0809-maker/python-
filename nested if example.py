salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    loan=int(input("loan amount:"))
    if(loan>=50000):
        print("amount proceed")
    else:
        print("eligible")
else:
    print("not")

q=int(input("q:"))
e=int(input("e:"))
if(q>=e):
    l=int(input("l:"))
    if(l<=e):
        print("oh goshh!!!")
    else:
        print("exicute")
else:
    print("nope")
