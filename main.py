from Users import User, session, create_user


def login():
    login = input("Login: ")
    password = input("Password: ")

    user = session.query(User).filter_by(Login=login).first()
        
    if user and user.Password == password:
        print("Login successful!")
    else:
        print("Login failed.")

def create_user_in_db():
    Login = input("Login: ")
    Password = input("Password: ")
    Email = input("Email: ")

    create_user(Login, Password, Email)


def main():
    print("1.Login")
    print("2.Create account")
    print("3.End session")
    choice = input('Choose: ')
 
    match choice: 
        case "login":
           login()
           
        case "create":
            create_user_in_db()
            pass
        case _:
            print("Incorrect")

if __name__ == "__main__":
    main()
