from connect import get_connection
import re 
pattern = r"^\+77\d{9}$"


def search():
    keyword = input("Search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (keyword,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


def add_or_update():
    name = input("Name: ")
    phone = input("Phone: ")
    if re.fullmatch(pattern,phone):
        email = input("Email: ")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
        "CALL upsert_contact(%s, %s, %s)",
        (name, phone, email)
    )
        conn.commit()
        conn.close()
    else: 
        print("The phone number is invalid")

def add_several_contacts():
    n = int(input("How many contacts?: ")) 

    names = []
    phones = []
    emails = []

    for _ in range(n):
        name = input("Name: ")

        while True:
            phone = input("Phone: ")
            if re.fullmatch(pattern, phone):
                break
            else:
                print("Invalid phone, try again")

        email = input("Email: ")

        names.append(name)
        phones.append(phone)
        emails.append(email)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL bulk_insert_contacts(%s, %s, %s)",
        (names, phones, emails)
    )

    conn.commit()
    conn.close()

def delete():
    value = input("Enter name or phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

    conn.close()


def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()

def showall():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close() 

def menu():
    while True:
        print("\n1. Search")
        print("2. Add/Update")
        print("3. Add Several Contacts")
        print("4. Delete")
        print("5. Pagination")
        print("6. Showall")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search()
        elif choice == "2":
            add_or_update()
        elif choice == "3":
            add_several_contacts()
        elif choice == "4":
            delete()
        elif choice == "5":
            pagination()
        elif choice == "6":
            showall()
        elif choice == "7":
            break


if __name__ == "__main__":
    menu()