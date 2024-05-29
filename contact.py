import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Contact Book")
        self.contacts = {}  # Dictionary to store contacts (name: phone number)

        # Create widgets
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)
        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_entry = tk.Entry(self.root)
        self.search_label = tk.Label(self.root, text="Search:")
        self.search_entry = tk.Entry(self.root)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_contact)
        self.update_button = tk.Button(self.root, text="Update", command=self.update_contact)
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_contact)

        # Layout widgets
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.phone_label.grid(row=1, column=0)
        self.phone_entry.grid(row=1, column=1)
        self.search_label.grid(row=4, column=0)
        self.search_entry.grid(row=4, column=1)
        self.search_button.grid(row=5, column=1)
        self.update_button.grid(row=2, column=1)
        self.delete_button.grid(row=3, column=1)

    def search_contact(self):
        name = self.search_entry.get()
        if name in self.contacts:
            phone = self.contacts[name]
            messagebox.showinfo("Contact Found", f"{name}: {phone}")
        else:
            messagebox.showinfo("Contact Not Found", f"{name} not in contacts.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.contacts[name] = phone
        messagebox.showinfo("Contact Updated", f"{name} updated with phone: {phone}")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Contact Deleted", f"{name} has been removed.")
        else:
            messagebox.showinfo("Contact Not Found", f"{name} not in contacts.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ContactBookApp()
    app.run()
