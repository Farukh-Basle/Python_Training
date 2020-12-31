def add(val1, val2):        #addition
    return val1 + val2

def sub(val1,val2):         #subtraction
    return val1 - val2

def mul(val1,val2):         #multiplication
    return val1 * val2

def div(val1,val2):         #division
    return val1 / val2

print("MY CALCULATOR")
print("=============")
print("1. ADD") 
print("2. SUB")
print("3. MUL")
print("4. DIV")
print("5. Exit")
print()
print("CHOOSE YOUR OPERATION: ")

while True:
    choice = input("Enter Your Choice (1/2/3/4/5): ")       #choose operation

    if choice in ('1', '2', '3', '4', '5'):                 #choose between 1 to 5
        val1 = float(input("Enter first Value: "))
        val2 = float(input("Enter second Value: "))


        if choice == '1':
            print(val1, '+', val2, '=' , add(val1, val2))

        elif choice == '2':
            print(val1 ,'-', val2, '=', sub(val1,val2))
        
        elif choice == '3':
            print(val1, '*', val2, '=', mul(val1, val2))
        
        elif choice == '4':
            print(val1, '/', val2, '=', div(val1, val2))

        elif choice == '5':
            exit

        break
    else:
        print("Invalid Input")