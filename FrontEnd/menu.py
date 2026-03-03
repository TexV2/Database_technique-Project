import main #Unnecessary?
from BackEnd import infrastructure as infrastructure
from BackEnd import contractors as contractors
from BackEnd import assignments as assignments
from BackEnd import log as log
from BackEnd import schema as schema
from BackEnd import helper as helper 


def schema_menu():
    while True:
        print ("\nChoose: ")
        print ("1) Reset all tables") #Unnecessary?
        print ("2) Show all tables")
        print ("b) Go back")
        choice = input("--> ").lower().strip()
        match choice:
            case "1":
                print("Do you want to reset with dummy data? y/n")
                choice = input ("--> ").lower().strip()
                if choice == "y":
                    schema.main_setup()
                elif choice == "n":
                    schema.main_setup(False)
                else:
                    print("Invalid input, please try again.")
            case "2":
                conn = schema.get_connection()
                curr = conn.cursor()
                helper.print_tables(curr)
                conn.close()
                curr.close()
            case "b":
                print ("Going back to main menu. ")
                return True
            case _:
                print("Invalid input, please try again.")  
        input("\nPress enter to continue...")



def infrastructure_submenu(menu_choice):
    def DRY(method):
        conn = main.get_connection()
        cur = conn.cursor()
        result, data = infrastructure.method_picker(method, cur)
        print()
        if result == -1:
            print("Invalid input, please try again.")
        elif result == 0:
            print("No data was found.")
        elif result == 1:  
            helper.print_tables(cur, "Infrastructure", f"{method} = {data}")
        cur.close()
        conn.close()

    while True:
        match menu_choice:
            case 3:
                print("Choose search method:")
                print("1) ID")
                print("2) Type")
                print("3) Location")
                print("4) Install date")
                print("5) Last inspection")
                print("6) State")
                print("b) Go back")
                choice = input("--> ").lower().strip()

                match choice:
                    case "1":
                        DRY("infrastructure_id")
                        return False
                    case "2":
                        DRY("type")
                        return False
                    case "3":
                        DRY("location")
                        return False
                    case "4":
                        DRY("install_date")
                        return False
                    case "5":
                        DRY("last_inspection")
                        return False
                    case "6":
                        DRY("state")
                        return False
                    case "b":
                        print("Going back to infrastructure menu. ")
                        return True
                    case _:
                        print("Invalid input, please try again.")
        input("\nPress enter to continue...")

def contractor_submenu(menu_choice):
    def DRY(method):
        conn = main.get_connection()
        cur = conn.cursor()
        result, data = infrastructure.method_picker(method, cur)
        print()
        if result == -1:
            print("Invalid input, please try again.")
        elif result == 0:
            print("No data was found.")
        elif result == 1:  
            helper.print_tables(cur, "Infrastructure", f"{method} = {data}")
        cur.close()
        conn.close()

    while True:
        match menu_choice:
            case 3:
                print("Choose search method:")
                print("1) ID")
                print("2) Type")
                print("3) Location")
                print("4) Install date")
                print("5) Last inspection")
                print("6) State")
                print("b) Go back")
                choice = input("--> ").lower().strip()

                match choice:
                    case "1":
                        DRY("infrastructure_id")
                        return False
                    case "2":
                        DRY("type")
                        return False
                    case "3":
                        DRY("location")
                        return False
                    case "4":
                        DRY("install_date")
                        return False
                    case "5":
                        DRY("last_inspection")
                        return False
                    case "6":
                        DRY("state")
                        return False
                    case "b":
                        print("Going back to infrastructure menu. ")
                        return True
                    case _:
                        print("Invalid input, please try again.")
        input("\nPress enter to continue...")

def infrastructure_menu():
    while True:
        skip = False
        print("\nChoose:")
        print("1) Show table")
        print("2) Add infrastructure")
        print("3) More information about a specific infrastructure")
        print("4) Update specific infrastructure")
        print("b) Go back")
        choice = input("--> ").lower().strip()
        match choice:
            case "1":
                conn = main.get_connection()
                cur = conn.cursor()
                print()
                helper.print_tables(cur, "Infrastructure")
            case "3":
                skip = infrastructure_submenu(3)
            case "b":
                print ("Going back to main menu. ")
                return True
            case _:
                print("Invalid input, please try again.")
        if not skip:
            input("\nPress enter to continue...")

def contractor_menu():
    while True:
        skip = False
        print("\nChoose:")
        print("1) Show table")
        print("2) Add contractor")
        print("3) More information about a specific contractor")
        print("4) Update specific contractor")
        print("b) Go back")
        choice = input("--> ").lower().strip()
        match choice:
            case "1":
                conn = main.get_connection()
                cur = conn.cursor()
                print()
                helper.print_tables(cur, "Contractor")
            case "3":
                skip = contractor_submenu(3)
            case "b":
                print ("Going back to main menu. ")
                return True
            case _:
                print("Invalid input, please try again.")
        if not skip:
            input("\nPress enter to continue...")




def menu():
    while True:
        skip = False
        print("\nChoose:")
        print("1) Schema commands ")
        print("2) Infrastructure commands ")
        print("3) Contractor commands ")
        print("4) Assignment commands ")
        print("5) Log commands")
        print("q) Quit")
        choice = input("--> ").lower().strip()
        
        match choice:
            case "1":
                skip = schema_menu()
            case "2":
                pass
                skip = infrastructure_menu()
            case "q":
                print("Goodbye.")
                return
            case _:
                print("Invalid input, please try again.")
        if not skip:
            input("\nPress enter to continue...")