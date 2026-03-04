from BackEnd import schema as schema
from BackEnd import helper as helper
VALID_COLUMNS = {"task_type", "projected_cost", "projected_start_date", "projected_end_date"}
def method_picker(method, cur):
    conversion = {
        "assignment_id": "the ID",
        "infrastructure_id": "the infrastructure id",
        "contractor ID": "the contractors id",
        "task_type": "the task type",
        "projected_cost": "the projected cost",
        "projected_start_date": "its projected start date",
        "projected_end_date": "it's projected end date"
    }
    data = input(f"Enter {conversion[method]}: ").lower().strip()
    if method == "assignment_id":
        try:
            data = int(data)
        except ValueError:
            return -1, data
    else:
        data = f"'{data}'"

    found_rows = check_rows(method, data, cur)
    if found_rows:
        return 1, data
    return 0, data

def remove_assignment(ID):
    conn = schema.get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM MaintenanceLog WHERE assignment_id = %s", 
                (ID,)
                )

    cur.execute(
        "DELETE FROM Assignment WHERE assignment_id = %s", 
        (ID,)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Assignment and related logs have been deleted")
    return

def update_assignment():
    print("Enter the ID of the assignment you would like to update")
    ID = input("--> ")
    print("Enter what column you would like to edit")
    column = input("--> ").lower()
    if column not in VALID_COLUMNS:
        print(f"Invalid column: {column}")
        return
    print("Enter the new value")
    new_value = input("--> ").lower()
    conn = schema.get_connection()
    cur = conn.cursor()
    cur.execute(
            f"UPDATE Assignment SET `{column}` = %s WHERE assignment_id =%s ",
            (new_value, ID)
        )
    conn.commit()
    cur.close()
    conn.close()
    return

def view_assignment_between_dates():
    print("What is the start date for the period you are looking for assignments in?")
    start_date = input("--> ")
    print("What is the end date for the period you are looking for assignments in?")
    end_date = input("--> ")
    conn = schema.get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM Assignment
        WHERE projected_start_date <= %s
        AND projected_end_date >= %s
    """,
    (end_date, start_date)
    )
    rows = cur.fetchall()
    print("ID  Infrastructure ID  Contractor ID  Task Type  Projected Cost  Projected Start Date    Projected End Date")
    for row in rows:
        print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}")
    cur.close()
    conn.close()
    return

def add_assignment():
    print("What is the ID of the contractor working on your assignment?")
    con_id = input("--> ")
    print("What is the ID of the infrastructure being worked on?")
    inf_id = input("--> ")
    print("What type of work is being done?")
    type = input("--> ")
    print("What is the projected cost?")
    cost = input("--> ")
    print("What is the projected start date?")
    start_date = input("--> ")
    print("What is the projected end date?")
    end_date = input("--> ")
    conn = schema.get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Assignment (contractor_id, infrastructure_id, task_type, projected_cost, projected_start_date, projected_end_date)" \
        "VALUES (%s, %s, %s, %s, %s, %s)", (con_id, inf_id, type, cost, start_date, end_date)
    )
    conn.commit()
    return True

def check_rows(method, data, cur):
    cur.execute(f"SELECT 1 FROM Assignment WHERE {method} = {data} LIMIT 1")
    found_rows = cur.fetchone() is not None
    if found_rows:
        return True
    return False

def DRY(method):
    conn = schema.get_connection()
    cur = conn.cursor()
    result, data = method_picker(method, cur)
    print()
    if result == -1:
        print("Invalid input, please try again.")
    elif result == 0:
        print("No data was found.")
    elif result == 1:  
        helper.print_tables(cur, "Assignment", f"{method} = {data}")
    cur.close()
    conn.close()