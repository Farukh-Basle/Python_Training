'''
#Continues loop
count = 0
while True:
    
    UserName = input("Enter Username : ")
    Password = input("Enter Password: ")

    count = count + 1
    if count == 3:
        print("You've reached the attempt limit, Please retry after sometime..")
        break
    else : 
        if UserName == 'Hardcode' and Password == 'Hardcode':
            print('You Have Logged in Successfully...')
            break
        else:
            count == count-1
            print('Please Check Username or Password and retry')
'''
#Main Program
count = 0
while True:
    
    UserName = input("Enter Username : ")       #enter username
    Password = input("Enter Password : ")       #enter password

    if UserName == 'Hardcode' and Password == 'Hardcode':       #defining username and password
            print('You Have Logged in Successfully...')         #if uname and pass correct then login
            break

    count = count + 1           #increment counter
    if count == 3:              #when counter reaches to 3 attempts
        print("You've reached the attempt limit, Please retry after sometime..")
        break 
        
    else:
        count == count-1        #decrement counter 
        print('Please Check Username or Password and retry')