from Users import User, session, create_user
from workout_generator.generators import WeekWorkoutPlanGenerator

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

def generate_plan_in_user_session():
    week_generator = WeekWorkoutPlanGenerator()
    able_to_train_days_per_week=[]
    for i in range(0,7):
        ableToTraindayOfWeek = input(f"Can u train in {i+1} day of week?[y/n]")
        if ableToTraindayOfWeek == "y":
            able_to_train_days_per_week.append(True)
        else:
            able_to_train_days_per_week.append(False)


    week_plan = week_generator.generate_week_fbw_plan(able_to_train_days_per_week)
    
    for day, plan in week_plan.items():
        print(f"{day}:")
        print(plan)
        print("\n" + "-"*30 + "\n")

def main():
    print("1.Login")
    print("2.Create account")
    print("3.End session")
    choice = input('Choose: ')
 
    match choice: 
        case "login":
           login()
           generate_plan_in_user_session()
               
           
        case "create":
            create_user_in_db()
            pass
        case _:
            print("Incorrect")

if __name__ == "__main__":
    main()
