class User:
    def __init__(self, username, master_password):
        self.username = username
        self.master_password = master_password

class PasswordEntry:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

class Vault:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def view_entries(self):
        for entry in self.entries:
            print(f"{entry.site} | {entry.username} | {entry.password}")

class PasswordManager:
    def __init__(self):
        self.vault = Vault()

    def add_password(self):
        site = input("Site: ")
        username = input("Username: ")
        password = input("Password: ")

        entry = PasswordEntry(site,username,password)
        self.vault.add_entry(entry)

    def show_password(self):
        self.vault.view_entries()

def main():
    manager = PasswordManager()

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3.Exit")

        choice = input("Choose: ")

        if choice == "1":
            manager.add_password()
        elif choice == "2":
            manager.show_password()
        elif choice == "3":
            break

main()