# login.py
import tkinter as tk
import csv
from tkinter import messagebox
from chat import start_chat_app  # This function will be defined in chat.py

def center_window(root, width, height):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates for the Tk root window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # Set the dimensions and position
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def verify_login(email, password):
    email = email.strip().lower()  # Normalize email
    password = password.strip()  # Assuming passwords are case-sensitive and should be trimmed

    with open('password.csv', newline='', encoding='utf-8-sig') as csvfile:  # Note the encoding change here
        reader = csv.reader(csvfile)
        for row in reader:
            stored_email = row[0].strip().lower()  # Normalize stored email
            stored_password = row[1].strip()  # Assuming passwords are case-sensitive and should be trimmed

            if stored_email == email and stored_password == password:
                return True
    return False


def attempt_login(email_entry, password_entry, root):
    email = email_entry.get()
    password = password_entry.get()
    if verify_login(email, password):
        root.destroy()  # Close the login window
        start_chat_app()  # Start the chat application
    else:
        messagebox.showerror("Login failed", "Invalid email or password")

def login_window():
    root = tk.Tk()
    center_window(root, 300, 150)  # Adjust the width and height as needed
    root.title("Login")
    root.geometry('300x150')

    tk.Label(root, text="Email:").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    login_button = tk.Button(root, text="Login", command=lambda: attempt_login(email_entry, password_entry, root))
    login_button.pack()

    root.mainloop()




