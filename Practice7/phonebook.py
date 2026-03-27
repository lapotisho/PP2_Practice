import csv
from connect import get_connection

def export_csv(file):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name, phone, email FROM contacts;")
    rows = cur.fetchall()

    with open(file, 'w', newline='') as f:
        import csv
        writer = csv.writer(f)
        writer.writerow(["name", "phone", "email"])
        writer.writerows(rows)

    conn.close()

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT
    );
    """)

    conn.commit()
    conn.close()

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)",
        (name, phone, email)
    )

    conn.commit()
    conn.close()


def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("New phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()
    conn.close()


def search_contact():
    keyword = input("Search name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s",
        (f"%{keyword}%",)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()


def delete_contact():
    name = input("Enter name to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name = %s",
        (name,)
    )

    conn.commit()
    conn.close()

def menu():
    while True:
        print("1. Import CSV")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Search")
        print("5. Delete")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == '1':
            export_csv("contacts.csv")
        elif choice == '2':
            add_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break

if __name__ == "__main__":
    create_table()
    menu()