from BackEnd import infrastructure as infrastructure
from BackEnd import contractors as contractors
from BackEnd import assignments as assignments
from BackEnd import log as log
from BackEnd import schema as schema
from BackEnd import helper as helper 


def schema_menu():
    while True:
        print ("\nSchema Menu: ")
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
    while True:
        match menu_choice:
            case 2:
                return infrastructure.add_infrastructure()
            case 3:
                print("\nChoose search method:")
                print("1) ID")
                
                print("b) Go back")
                choice = input("--> ").lower().strip()
                match choice:
                    case "1":
                        infrastructure.DRY("infrastructure_id")
                        return False
                    case "b":
                        print("Going back to infrastructure menu. ")
                        return True
                    case _:
                        print("Invalid input, please try again.")
            case 4:
                return infrastructure.update_infrastructure()
            case 5:
                print("Enter the ID of the infrastructure you want to remove (enter 'b' to go back).")
                print("Removing a infrastructure will remove related assignments and logs.")
                choice = input("--> ").lower().strip()
                if choice == "b":
                    return True
                else:
                    print("Are you sure? y/n")
                    double_check = input("--> ").lower().strip()
                    if double_check[0] == "y":
                        infrastructure.remove_infrastructure(choice)
                        return False
                    elif double_check[0] == "n":
                        return True
                    else:
                        print("Invalid input, please try again later")
                        return False
        input("\nPress enter to continue...")

def assignment_submenu(menu_choice):
    while True:
        match menu_choice:
            case 2:
                return assignments.add_assignment()
            case 3:
                assignments.view_assignment_between_dates()
                input("Press enter to continue...")
                return True
            case 4:
                print("Choose search method:")
                print("1) ID")
                print("b) Go back")
                choice = input("--> ").lower().strip()
                match choice:
                    case "1":
                        assignments.DRY("assignment_id")
                        return False
                    case "b":
                        print("Going back to assignment menu. ")
                        return True
                    case _:
                        print("Invalid input, please try again.")
            case 5:
                return assignments.update_assignment()
            case 6:
                print("Enter the ID of the assignment you want to remove (enter 'b' to go back).")
                choice = input("--> ").lower().strip()
                if choice == "b":
                    return True
                else:
                    print("Are you sure? y/n")
                    double_check = input("--> ").lower().strip()
                    if double_check[0] == "y":
                        assignments.remove_assignment(choice)
                        return False
                    elif double_check[0] == "n":
                        return True
                    else:
                        print("Invalid input, please try again later")
                        return False
        input("\nPress enter to continue...")

def log_submenu(menu_choice):
    while True:
        match menu_choice:
            case 2:
                return log.add_log()
            case 3:
                log.view_log_between_dates()
                input("Press enter to continue")
                return True
            case 4:
                print("Choose search method:")
                print("1) ID")
                print("b) Go back")
                choice = input("--> ").lower().strip()
                match choice:
                    case "1":
                        log.DRY("assignment_id")
                        return False
                    case "b":
                        print("Going back to assignment menu. ")
                        return True
                    case _:
                        print("Invalid input, please try again.")
            case 5:
                return log.update_log()
            case 6:
                print("Enter the ID of the maintenance log you want to remove (enter 'b' to go back).")
                choice = input("--> ").lower().strip()
                if choice == "b":
                    return True
                else:
                    print("Are you sure? y/n")
                    double_check = input("--> ").lower().strip()
                    if double_check[0] == "y":
                        log.remove_log(choice)
                        return False
                    elif double_check[0] == "n":
                        return True
                    else:
                        print("Invalid input, please try again later")
                        return False
        input("\nPress enter to continue...")

def contractor_submenu(menu_choice):
    while True:
        match menu_choice:
            case 2:
                return contractors.add_contractor()
            case 3:
                print("Choose search method:")
                print("1) ID")
                print("2) Name")
                print("b) Go back")
                choice = input("--> ").lower().strip()
                match choice:
                    case "1":
                        contractors.DRY("Contractor_id")
                        return False
                    case "2":
                        contractors.DRY("Name")
                        return False
                    case "b":
                        print("Going back to infrastructure menu. ")
                        return True
                    case _:
                        print("Invalid input, please try again.")
            case 4:
                return contractors.update_contractor()
            case 5:
                print("Enter the ID of the contractor you want to remove (enter 'b' to go back).")
                print("Removing a contractor will remove related assignments and logs.")
                choice = input("--> ").lower().strip()
                if choice == "b":
                    return True
                else:
                    print("Are you sure? y/n")
                    double_check = input("--> ").lower().strip()
                    if double_check[0] == "y":
                        contractors.remove_contractor(choice)
                        return False
                    elif double_check[0] == "n":
                        return True
                    else:
                        print("Invalid input, please try again later")
                        return False
        input("\nPress enter to continue...")

def infrastructure_menu():
    while True:
        skip = False
        print("\nInfrastructure Menu:")
        print("1) Show table")
        print("2) Add infrastructure")
        print("3) More information about a specific infrastructure")
        print("4) Update specific infrastructure")
        print("5) Remove specific infrastructure")
        print("b) Go back")
        choice = input("--> ").lower().strip()
        match choice:
            case "1":
                conn = schema.get_connection()
                cur = conn.cursor()
                print()
                helper.print_tables(cur, "Infrastructure")
            case "2":
                skip = infrastructure_submenu(2)
            case "3":
                skip = infrastructure_submenu(3)
            case "4":
                skip = infrastructure_submenu(4)
            case "5":
                skip = infrastructure_submenu(5)
            case "b":
                print ("Going back to main menu. ")
                return True
            case _:
                print("Invalid input, please try again.")
        if not skip:
            input("\nPress enter to continue...")

def log_menu():
    while True:
        skip = False
        print("\nAssignment Log Menu:")
        print("1) Show table")
        print("2) Add log")
        print("3) View logs between two dates")
        print("4) More information about a specific log")
        print("5) Update log")
        print("6) Remove specific log")
        print("b) Go back")
        choice = input("--> ").lower().strip()
        match choice:
            case "1":
                conn = schema.get_connection()
                cur = conn.cursor()
                print()
                helper.print_tables(cur, "MaintenanceLog")
            case "2":
                skip = log_submenu(2)
            case "3":
                skip = log_submenu(3)
            case "4":
                skip = log_submenu(4)
            case "5":
                skip = log_submenu(5)
            case "6":
                skip = log_submenu(6)
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
        print("\nContractor Menu:")
        print("1) Show table")
        print("2) Add contractor")
        print("3) More information about a specific contractor")
        print("4) Update specific contractor")
        print("5) Remove specific contractor")
        print("b) Go back")
        choice = input("--> ").lower().strip()
        match choice:
            case "1":
                conn = schema.get_connection()
                cur = conn.cursor()
                print()
                helper.print_tables(cur, "Contractor")
            case "2":
                skip = contractor_submenu(2)
            case "3":
                skip = contractor_submenu(3)
            case "4":
                skip = contractor_submenu(4)
            case "5":
                skip = contractor_submenu(5)
            case "b":
                print ("Going back to main menu. ")
                return True
            case _:
                print("Invalid input, please try again.")
        if not skip:
            input("\nPress enter to continue...")

def assignment_menu():
    while True:
        skip = False
        print("\nAssignment Menu:")
        print("1) View assignments")
        print("2) Add assignment")
        print("3) View assignments ongoing during certain dates")
        print("4) View specific assignment")
        print("5) Update assignment")
        print("6) Remove assignment")
        print("b) Go Back")
        choice = input("--> ").lower().strip()
        match choice:
            case "1":
                conn = schema.get_connection()
                cur = conn.cursor()
                print()
                helper.print_tables(cur, "Assignment")
            case "2":
                skip = assignment_submenu(2)
            case "3":
                skip = assignment_submenu(3)
            case "4":
                skip = assignment_submenu(4)
            case "5":
                skip = assignment_submenu(5)
            case "6":
                skip = assignment_submenu(6)
            case "b":
                print("Going back to the main menu")
                return True
        if not skip:
            input("\nPress enter to continue...")


def menu():
    while True:
        skip = False
        print("\nMain Menu:")
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
                skip = infrastructure_menu()
            case "3":
                skip = contractor_menu()
            case "4":
                skip = assignment_menu()
            case "5":
                skip = log_menu()
            case "q":
                print("Goodbye.")
                return
            case _:
                print("Invalid input, please try again.")
        if not skip:
            input("\nPress enter to continue...")