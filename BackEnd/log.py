from BackEnd import schema as schema
from BackEnd import helper as helper
VALID_COLUMNS = {"start_date", "end_date", "cost", "result", "review"}
def method_picker(method, cur):
    conversion = {
        "assignment_id": "the assignment ID",
        "result": "the result",
        "review": "a review of the contractor",
        "cost": "cost",
        "start_date": "the start date",
        "end_date": "the end date"
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

def remove_log(ID):
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

def update_log():
    print("Enter the assignment ID of the log you would like to update")
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
            f"UPDATE MaintenanceLog SET `{column}` = %s WHERE assignment_id =%s ",
            (new_value, ID)
        )
    conn.commit()
    cur.close()
    conn.close()
    return

def view_log_between_dates():
    print("What is the start date for the period you are looking for logs in?")
    start_date = input("--> ")
    print("What is the end date for the period you are looking for logs in?")
    end_date = input("--> ")
    conn = schema.get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM MaintenanceLog
        WHERE start_date <= %s
        AND end_date >= %s
    """,
    (end_date, start_date)
    )
    rows = cur.fetchall()
    print("Assignment ID  Start Date  End Date  Cost  Result  Review ")
    for row in rows:
        print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")
    cur.close()
    conn.close()
    return

def add_log():
    print("What is the id for the logs assignment?")
    ass_id = input("--> ")
    print("What is the start date?")
    start_date = input("--> ")
    print("What is the end date?")
    end_date = input("--> ")
    print("What was the actual cost?")
    cost = input("--> ")
    print("What was the result?")
    result = input("--> ")
    print("How would you review the contractors performance?")
    review = input("--> ")
    conn = schema.get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO MaintenanceLog (assignment_id, start_date, end_date, cost, result, review)" \
        "VALUES (%s, %s, %s, %s, %s, %s)", (ass_id, start_date, end_date, cost, result, review)
    )
    conn.commit()
    return True

def check_rows(method, data, cur):
    cur.execute(f"SELECT 1 FROM MaintenanceLog WHERE {method} = {data} LIMIT 1")
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
        helper.print_tables(cur, "MaintenanceLog", f"{method} = {data}")
    cur.close()
    conn.close()