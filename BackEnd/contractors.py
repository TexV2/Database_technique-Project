def method_picker(method, cur):
    conversion = {
        "Contractor_id": "the ID",
        "Name": "Contractor name",
        "Rating": "the rating",
        "Field": "the field",
        "Cost": "the Cost",
    }
    data = input(f"Enter {conversion[method]}: ").lower().strip()
    if method == "Contractor_id":
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


def check_rows(method, data, cur):
    cur.execute(f"SELECT 1 FROM Contractor WHERE {method} = {data} LIMIT 1")
    found_rows = cur.fetchone() is not None
    if found_rows:
        return True
    return False