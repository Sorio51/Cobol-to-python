from operations import run_operation

def main():
    continue_flag = True
    while continue_flag:
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        choice = input("Enter your choice (1-4): ")
        try:
            user_choice = int(choice)
        except ValueError:
            user_choice = 0

        if user_choice == 1:
            run_operation("TOTAL")
        elif user_choice == 2:
            run_operation("CREDIT")
        elif user_choice == 3:
            run_operation("DEBIT")
        elif user_choice == 4:
            continue_flag = False
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice, please select 1-4.")

if __name__ == "__main__":
    main()
