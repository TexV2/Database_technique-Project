from dotenv import load_dotenv
from BackEnd import schema as schema
from FrontEnd import menu

#Just the menu
def main():
    load_dotenv()
    schema.main_setup()
    menu.menu()

if __name__ == "__main__":
    main()


"""
TODO
* At least two of the five queries should deal with data from more than one table, i.e.,
    you should use at least two multirelation queries
"""