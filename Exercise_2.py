n1 = int(input("Please enter a number : "))
rem1 = n1%2
if (rem1 == 0):
    print(str(n1) +" is an even number.")
else:
    print(str(n1) +" is an odd number.")
print("_______________________________________________________________")
    
#=========================================================================================================

def Extra_1():
    rem2 = n1%4
    if (rem2 == 0):
        print(str(n1) +" is a multiple of 4.")
    else:
        print(str(n1) +" is not a multiple of 4.")

def Extra_2():
    num = int(input("Enter an integer : "))
    chk = int(input("Enter another integer : "))
    div = num%chk
    if (div == 0):
        print(str(chk) + " divides " + str(num) + " evenly.")
    else:
        print(str(chk) + " does not divide " + str(num) + " evenly.")
#=========================================================================================================

def perm():
    while True:
        p = input("Do you want to run the extra program (Y/N) : ")
        if(p == "Y"):
            a = input("Please select the program you would like to run (1/2) : ")
            if(a == "1"):
                print("Program 1 Executing----")
                Extra_1()
                break
            elif(a == "2"):
                print("Program 2 Executing----")
                Extra_2()
                break
            print("Please select a valid program (1/2)")          
        elif(p == "N"):
            print("____________________________END_____________________________")
            break
        print("Please provide a valid input (Y/N)")

perm()

print("==================================================================")
            
        
        
        
    
    
    
