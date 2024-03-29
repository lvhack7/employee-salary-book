import readchar
from assignG0234_backEnd import add_entry, view_entries, delete_entries

def main():

    # Printing ASCII Welcome message
    welcome_message = """
============================================
|                                          |      
|      WELCOME TO EMPLOYEE SALARY BOOK     |       
|                                          |
============================================                                
    """
    print(welcome_message)
    
    while True:
        # Printing a user menu
        print("\n" + "=" * 30)
        print("|{:^28}|".format("Menu"))
        print("=" * 30)
        print("|{:^28}|".format("1. Add a new entry"))
        print("|{:^28}|".format("2. View/display all entries"))
        print("|{:^28}|".format("3. Delete all entries"))
        print("|{:^28}|".format("4. Exit the program"))
        print("=" * 30)
        
        # Making the user choose the options using input() function
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            delete_entries()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        # Error handling of wrong option
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

        # Checking if any key is pressed using readchar module to continue the loop
        print("Press any key to continue...")
        k = readchar.readchar()

if __name__ == "__main__":
    main()