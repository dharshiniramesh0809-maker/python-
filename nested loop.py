for i in range(1,4):
    print("week:",i)
    for j in range(1,4):
     print("day:",j)
    

for i in range(1,5):
    print("*")
    for j in range(i):
        print(j,end="")



# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
   print(fruit)
# Using range
for i in range(4):
   print(i) # Prints 0 to 3

count = 0
while count < 3:
   print("Hello Geek")
   count += 1



for i in range(1, 4):
   for j in range(i):
       print(i, end=' ')
   print()


colors = {'apple': 'red', 'banana': 'yellow'}
for fruit, color in colors.items():
   print(f"The {fruit} is {color}.")
    
    
    
