from getpass import getpass
islogin = False
login_attempt = 0

username = "davez123"
password = "davezpoge1"

while islogin == False:
    user = input("Enter username: ")
    pswrd = input("Enter password: ")

    if user == username and pswrd == password:
        print("Login Successfully")
        print("Number of Login attempts", login_attempt)
        islogin == True 
        break
    else:
        print("Incorrect username and password")
        login_attempt += 1
        islogin == False
        continue