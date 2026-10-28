import tkinter as tk
from tkinter import ttk, messagebox 
#ttk: provides themed widgets and styling support.
#messagebox: Displays error, warning, and information dialogs.
from pathlib import Path
#path: Handles file and folder paths.
import sys


cli_path = Path(__file__).resolve().parent.parent / "cli"
sys.path.insert(0, str(cli_path))
#sys.path: Lists the locations Python searches for modules.
from database import Database
from student_system import validate_email, validate_password
from Enrolment_window import show_enrolment_window
#imports the page function from another file in the same gui folder.
database = Database()

window = tk.Tk()
window.title("CLIUniApp")
window.geometry("1280x832")
window.configure (bg="#F8FAFC")

login_frame = tk.Frame(window, bg="#FFFFFF")
#Create a white container inside the main window
login_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=400,
    height=460
)

title_label = tk.Label(
    login_frame,
    text="Sign in",
    bg="#1E3A8A",
    fg="#FFFFFF",
    font=("Arial", 28, "bold"),
    pady=35
)
title_label.pack(fill="x")

form_frame = tk.Frame(login_frame, bg="#FFFFFF")
form_frame.pack(fill="x", padx=24, pady=20)
#fill="x": Fill the available horizontal space
email_label = tk.Label(
    form_frame,
    text="Email",
    bg="#FFFFFF",
    fg="#0F172A",
    font=("Arial", 12)
)
email_label.pack(anchor="w")
#anchor="w", w means west, aligns the label to the left.
email_entry = tk.Entry(
    #Entry: a single-line input widget
    form_frame,
    font=("Arial", 14),
    relief="solid",
    bd=1
)
email_entry.pack(fill="x", ipadx=6, ipady=8, pady=(6, 16))
#Set the entry spacing
password_label = tk.Label(
    form_frame,
    text="Password",
    bg="#FFFFFF",
    fg="#0F172A",
    font=("Arial", 12)
)
password_label.pack(anchor="w")

password_entry = tk.Entry(
    form_frame,
    font=("Arial", 14),
    relief="solid",
    bd=1,
    show="*"
)
password_entry.pack(fill="x", ipadx=6, ipady=8, pady=(6, 16))
style = ttk.Style(window)
style.theme_use("clam")
style.configure(
    "Login.TButton",
    font=("Arial", 12, "bold"),
    background="#1E3A8A",
    foreground="#FFFFFF",
    relief="flat",
    padding=(0,12),
    borderwidth=0
)
style.map(
    "Login.TButton",
    background=[
        ("pressed", "#172554"),
        ("active", "#1E40AF")
    ]
)
def show_login():
    password_entry.delete(0, tk.END)
    login_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        width=400,
        height=460
    )
def login():
    email = email_entry.get().strip()
    password = password_entry.get()
    if not validate_email(email) or not validate_password(password):
        messagebox.showerror(
            "Invalid format",
            "Incorrect email or password format.",
            parent=window
        )
        return
    existing_record = database.find_record_by_email(email)
    if existing_record is None:
        messagebox.showerror(
            "Login failed",
            "Incorrect email or password.",
            parent=window
        )
        return
    if existing_record["password"] != password:
        messagebox.showerror(
            "Login failed",
            "Incorrect email or password.",
            parent=window    
        )
        return
    login_frame.place_forget()
    #place_forget() hides the login container without destroying it, allowing it to be displayed again after logout.
    show_enrolment_window(
        window,
        existing_record,
        show_login
    )
login_button = ttk.Button(
    form_frame,
    text="Sign in",
    style="Login.TButton",
    command=login
)
login_button.pack(fill="x", pady=(8, 0))
window.mainloop()