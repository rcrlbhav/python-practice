import random

i1 = int(input("What should the length of the first list be? :"))
i2 = int(input("What about the second list? :"))

l1 = list(random.randrange(1,100) for i in range(i1))
l2 = list(random.randrange(1,100) for i in range(i2))

print("The first list is: ",l1)
print("The second list is: ",l2)


com = []

for n in l1:
    if n in l2 and n not in com:
        com.append(n)

if com:
    print("The common numbers from the above lists are :",com)
else:
    print("There are no common values.")
