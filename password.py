import os # always before ending the program press "12" to exit
import sqlite3
import bcrypt
import secrets
import string
from getpass import getpass
from cryptography.fernet import Fernet
from datetime import datetime, timedelta

# Database and encryption setup
DB_FILE = "passwords.db"
KEY_FILE = "secret.key"
MASTER_PWD_FILE = "master_pwd.hash"
BACKUP_FILE = "backup_passwords.enc"
PASSWORD_EXPIRY_DAYS = 90

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

if not os.path.exists(KEY_FILE):
    generate_key()

key = load_key()
fernet = Fernet(key)

# Master password setup
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password)

if not os.path.exists(MASTER_PWD_FILE):
    master_pwd = getpass("Set your master password: ")
    with open(MASTER_PWD_FILE, "wb") as pwd_file:
        pwd_file.write(hash_password(master_pwd))
else:
    master_pwd = getpass("Enter your master password: ")
    with open(MASTER_PWD_FILE, "rb") as pwd_file:
        stored_pwd = pwd_file.read()
        if not check_password(stored_pwd, master_pwd):
            print("Incorrect master password.")
            exit()

# SQLite database setup
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                    service TEXT, 
                    password TEXT,
                    last_updated TEXT
                  )''')
conn.commit()

def encrypt_password(password):
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password).decode()

def save_password(service, password):
    encrypted_password = encrypt_password(password)
    last_updated = datetime.now().isoformat()
    cursor.execute("INSERT INTO passwords (service, password, last_updated) VALUES (?, ?, ?)", 
                   (service, encrypted_password, last_updated))
    conn.commit()

def retrieve_password(service):
    cursor.execute("SELECT password, last_updated FROM passwords WHERE service=?", (service,))
    result = cursor.fetchone()
    if result:
        password, last_updated = result
        if (datetime.now() - datetime.fromisoformat(last_updated)) > timedelta(days=PASSWORD_EXPIRY_DAYS):
            print(f"Warning: The password for {service} hasn't been updated for over {PASSWORD_EXPIRY_DAYS} days.")
        return decrypt_password(password)
    else:
        return None

def delete_password(service):
    cursor.execute("DELETE FROM passwords WHERE service=?", (service,))
    conn.commit()

def update_password(service, password):
    encrypted_password = encrypt_password(password)
    last_updated = datetime.now().isoformat()
    cursor.execute("UPDATE passwords SET password=?, last_updated=? WHERE service=?", 
                   (encrypted_password, last_updated, service))
    conn.commit()

def list_services():
    cursor.execute("SELECT service FROM passwords")
    services = cursor.fetchall()
    return [service[0] for service in services]

def search_services(keyword):
    cursor.execute("SELECT service FROM passwords WHERE service LIKE ?", ('%' + keyword + '%',))
    services = cursor.fetchall()
    return [service[0] for service in services]

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def backup_passwords():
    cursor.execute("SELECT * FROM passwords")
    data = cursor.fetchall()
    encrypted_data = fernet.encrypt(str(data).encode())
    with open(BACKUP_FILE, "wb") as backup_file:
        backup_file.write(encrypted_data)
    print("Backup completed successfully.")

def restore_passwords():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "rb") as backup_file:
            encrypted_data = backup_file.read()
            data = eval(fernet.decrypt(encrypted_data).decode())
            cursor.executemany("INSERT INTO passwords (service, password, last_updated) VALUES (?, ?, ?)", data)
        conn.commit()
        print("Restore completed successfully.")
    else:
        print("No backup file found.")

def view_passwords():
    cursor.execute("SELECT service, password FROM passwords")
    passwords = cursor.fetchall()
    for service, password in passwords:
        print(f"Service: {service}, Password: {decrypt_password(password)}")
    export = input("Do you want to export passwords to a file? (yes/no): ")
    if export.lower() == 'yes':
        with open("exported_passwords.txt", "w") as f:
            for service, password in passwords:
                f.write(f"Service: {service}, Password: {decrypt_password(password)}\n")
        print("Passwords exported successfully.")

def set_password_expiry():
    global PASSWORD_EXPIRY_DAYS
    days = int(input("Enter the number of days for password expiry: "))
    PASSWORD_EXPIRY_DAYS = days
    print(f"Password expiry set to {PASSWORD_EXPIRY_DAYS} days.")

def close_program():
    backup_passwords()
    conn.close()
    print("Program closed and backup created.")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Update a password")
        print("4. Delete a password")
        print("5. List all services")
        print("6. Generate a strong password")
        print("7. Backup passwords")
        print("8. Restore passwords")
        print("9. Search for a service")
        print("10. View all passwords")
        print("11. Set password expiry period")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            pwd = getpass("Enter the password: ")
            save_password(service, pwd)
            print(f"Password for {service} saved successfully!")
        elif choice == "2":
            service = input("Enter the service name: ")
            pwd = retrieve_password(service)
            if pwd:
                print(f"Password for {service}: {pwd}")
            else:
                print(f"No password found for {service}.")
        elif choice == "3":
            service = input("Enter the service name: ")
            if retrieve_password(service):
                pwd = getpass("Enter the new password: ")
                update_password(service, pwd)
                print(f"Password for {service} updated successfully!")
            else:
                print(f"No password found for {service}.")
        elif choice == "4":
            service = input("Enter the service name: ")
            if retrieve_password(service):
                delete_password(service)
                print(f"Password for {service} deleted successfully!")
            else:
                print(f"No password found for {service}.")
        elif choice == "5":
            services = list_services()
            if services:
                print("Stored services:")
                for service in services:
                    print(f"- {service}")
            else:
                print("No services found.")
        elif choice == "6":
            length = int(input("Enter the desired password length: "))
            pwd = generate_password(length)
            print(f"Generated password: {pwd}")
        elif choice == "7":
            backup_passwords()
        elif choice == "8":
            restore_passwords()
        elif choice == "9":
            keyword = input("Enter the service name keyword to search: ")
            services = search_services(keyword)
            if services:
                print("Matching services:")
                for service in services:
                    print(f"- {service}")
            else:
                print("No matching services found.")
        elif choice == "10":
            view_passwords()
        elif choice == "11":
            set_password_expiry()
        elif choice == "12":
            close_program()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
