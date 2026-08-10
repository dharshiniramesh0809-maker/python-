for i in range(1,11):
    if(i%2==0):
        print(i,"even")
    else:
        print(i,"odd")




o_count=0
p_count=0
for i in range(1,11):
    if(i%2==0):
        o_count=o_count+1
    else:
        p_count=p_count+1
print(o_count)
print(p_count)
        
        
ir_count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        ir_count=ir_count+1
print(ir_count)


sum=0
for i in range(1,6):
    sum=sum+i
    print(sum)



a=[]
print("enter 10 number:")
for i in range(10):
    num=int(input("enter"+str(i+1)))
    a.append(num)
    print(a)

    avg=0
    for i in a:
        avg=avg+i
        print(avg)



