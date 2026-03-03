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