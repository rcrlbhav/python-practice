from datetime import date
year = date.today().year

class User_Input:
    age = 18

User1 = User_Input()
User1.age = int(input("How old are you? : "))

age_left = 100 - User1.age
y = year + age_left
year_turn = str(y)


result = "\n"+"You will be 100 years old in the year "+year_turn+"."
   

print(result)
print("==============================================================================")

perm = 'X'
mul = 1

def Extra_1(perm,mul):
    while True:
        perm = input("Do you want to run the extra program? (Y/N): ")
        if(perm == "Y"):
            print("______________________________________________________________________________")
            mul = int(input("Enter a random integer: "))
            print("______________________________________________________________________________")
            print(result*mul)
            print("______________________________________________________________________________")
            break
            
        elif(perm == "N"):
            print("_______________________________________END____________________________________")
            break
            
        print("Please provide a valid input(Y/N)")
        
    
Extra_1(perm,mul)
