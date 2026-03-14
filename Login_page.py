import shopping_system as shopping

Users_list = {
    "admin@gmail.com": {"id": 1, "username": "XxTheAdminxX", "password": "Im_the_admin_123", "status": "admin"}
}

def space_divider():
    print(" ")
    print("/"*28)
    





def Log_in():
    space_divider()
    print("----------LOG IN ----------")
    print("‼️", "Enter \"Exit\" to go back to menu", "‼️")
    
    
    while True:
        email = input("Enter your email: ")
        
        
        if email in Users_list.keys():
            name = Users_list[email]["username"]
            
            while True:
                password = input("Enter your password: ")
                
                if password == Users_list[email]["password"]:
                    
                    if "admin" == Users_list[email]["status"]: 
                        admin_page(name)
                    else:
                        user_page(name)
                    #When they log out:
                    space_divider()
                    return
                
                elif password == "Exit":
                    space_divider()
                    return
                else:
                    print("Incorrect password, please try again or Exit")
        
        elif email == "Exit":
            space_divider()
            return
        else:
            print("Email doesn't exist, please try again or Exit")





def Sign_up():
    space_divider()
    print("----------SIGN UP ----------")
    print("‼️", "Enter \"Exit\" to go back to menu", "‼️")
    
    username = input("Create a username: ")
    if username == "Exit":
        space_divider()
        return
    
    while True:
        email = input("Enter your email: ")
        
        if email == "Exit":
            space_divider()
            return        

        elif email not in Users_list.keys():
            while True:
                password1 = input("Enter your password: ")
                password2 = input("Confirm your password: ")
                
                if password1 == "Exit" or password2 == "Exit":
                    space_divider()
                    return 
                               
                elif password1 == password2:
                    Users_list[email] = {"id": len(Users_list)+1, "username": username, "password": password1, "status": "user"}
                    space_divider()
                    print("Account successfully created!!, Now you can log in")
                    space_divider()
                    return

                else:
                    print("Passwords doesn't match, try again")

        else:
            print("Email already registered, try a different one or Exit")





def user_page(name):
    space_divider()
    print(f"Hi {name}, welcome back!")
    shopping.menu()
    return





def admin_page(name):
    space_divider()
    print(f"Hi Boss {name}, welcome back")
    shopping.admin_menu()    
    return





def main_menu():
    while True:
        print("------HOME MENU------")
        print("Hi, welcome to MyShop.com")
        print("1) Log in")
        print("2) Sign up")
        print("3) Exit")
        space_divider()
        
        option = input("enter an option to continue: ")
        match option:
            case "1":
                Log_in()
            case "2":
                Sign_up()
            case "3":
                space_divider()
                print("Thanks for visiting us, see you next time!")
                return
            case _:
                print("PLEASE ENTER A VALID OPTION")





#START OF THE PROGRAM
main_menu()


