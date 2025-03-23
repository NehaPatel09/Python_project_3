import time

class AttemptExceptionError(Exception):
    pass

def authenticate():
    username = "user_1234"
    password = "userpass@98765"
    attempts = 1  

    while attempts < 4:
        user_input = input("Enter your username: ")
        user_pass = input("Enter your password: ")

        if user_input == username and user_pass == password:
            print("Login successful!")
            return  
        else:
            attempts += 1
            print("Invalid credentials. Try again.")

        if attempts == 4:
            try:
                raise AttemptExceptionError("Too many attempts! Try again after 1 hour.")
            except AttemptExceptionError as e:
                print(e)
                time.sleep(3600)  
                return  
authenticate()
