unum = int(input("Enter an integer of your choice : "))
ulist = list(range(1,unum+1))
fac = []

for num in ulist:
    if (unum % num == 0):
        fac.append(num)
print("The factors list is given below : ")
print(fac)
