#Given list : a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#===========================================================================================

numlist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
nl = []

def main():
    for num in numlist:
        if (num < 5):
            nl.append(num)
        else:
            break
    print(nl)
        
main()

#===========================================================================================

def Extra():
    ull = []
    ulh = []
    unum = int(input("Enter an integer of your choice : "))
    for num in numlist:
        if (num < unum):
            ull.append(num)
        elif(num >= unum):
            ulh.append(num)           
    print("Filtered List is:",ull)

def Perm():
    while True:
        p = input("Extra Program? (Y/N) : ")
        if (p == "Y"):
            Extra()
            break
        elif (p == "N"):
            print("___________________________EOP___________________________")
            break
        
        print("Make a valid choice (Y/N) : ")

Perm()

print("=========================================================================")
        
    
               
