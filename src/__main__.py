def add_entry(records, username, email, displayName):
    records.append({"username": username, "email": email, "displayName": displayName})
    return records


def show(records):
    for record in records:
        print(record["username"], record["email"], record["displayName"])


def main():
    records = []

    while True:
        username = input("username: ")
        if username == "":
            break
        if username in [ "admin", "root", "morderator", "mod", "null"]:
            print("Invalid username. Please try again.")
            break
        email = input("Email: ")
        if email == "":
            break
        if "@" not in email or "." not in email:
            print("Invalid email. Please try again.")
            break
        displayName = input("Display Name: ")
        if displayName == "":
            break
        if len(displayName) < 3:
            print ("Display name must be between 3 and 20 characters.")
            break
        if not displayName.isalnum():
            print("Display name must contain only letters and numbers.")
            break
        if displayName in [ "admin", "root", "morderator", "mod", "null"]:
            print("Invalid display name. Please try again.")
            break
        if displayName.startswith (tuple('0123456789')):
            print("Display name cannot start with a number.")
            break
        records = add_entry(records, username, email, displayName)

    show(records)

if __name__ == "__main__":
    main()