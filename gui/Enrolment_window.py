import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from subject import Subject
from student_system import validate_password
from Subject_window import show_subject_window

def show_enrolment_window(window, student_record, on_logout):
    database = Database()

    enrolment_frame = tk.Frame(window, bg="#F8FAFC")
    enrolment_frame.pack(fill="both", expand=True)

    header_frame = tk.Frame(enrolment_frame, bg="#FFFFFF")
    header_frame.pack(fill="x")

    welcome_label = tk.Label(
        header_frame,
        text=f"Welcome, {student_record['name']}",
        bg="#FFFFFF",
        fg="#1E3A8A",
        font=("Arial", 14, "bold")
    )
    welcome_label.pack(side="left", padx=24, pady=20)
    
    def logout():
        enrolment_frame.destroy()
        on_logout()

    logout_button = ttk.Button(
        header_frame,
        text="Log out",
        style="Login.TButton",
        command=logout #The function runs when the button is clicked.
    )
    logout_button.pack(side="right", padx=24, pady=16)

    def view_subjects():
        show_subject_window(window, student_record)

    subject_button = ttk.Button(
        header_frame,
        text="My Subjects",
        style="Login.TButton",
        command=view_subjects,
        width=16
    )
    subject_button.pack(side="right", padx=(0,12), pady=16)
    #receives the current student record
    
    title_label = tk.Label(
        enrolment_frame,
        text="Subject Enrolment",
        bg="#F8FAFC",
        fg="#1E3A8A",
        font=("Arial", 24, "bold")
    )
    title_label.pack(anchor="w", padx=48, pady=(36, 20))

    content_frame = tk.Frame(enrolment_frame, bg="#F8FAFC")
    content_frame.pack(fill="x", padx=48)

    count_label = tk.Label(
        content_frame,
        text=f"Enrolled subjects: {len(student_record['subjects'])} / 4",
        #len: Gets the number of subjects enrolled by this student
        bg="#F8FAFC" ,
        fg="#0F172A",
        font=("Arial", 12)
    )
    count_label.pack(anchor="e", pady=(0, 12))
#anchor="e": Aligns the count label to the right; e means east.
    subject_table = ttk.Treeview( #Creates a Treeview widget used here as a flat table.
        content_frame,
        columns=("subject_id", "mark", "grade"),
        #Defines the internal identifiers for the three columns.
        show="headings",
        selectmode="browse",
        height=8
    )
    subject_table.heading("subject_id", text="Subject ID")
    subject_table.heading("mark", text="Mark")
    subject_table.heading("grade", text="Grade")
    
    subject_table.column("subject_id", width=200, anchor="center")
    subject_table.column("mark", width=150, anchor="center")
    subject_table.column("grade", width=150, anchor="center")

    subject_table.pack(fill="x")

    for subject in student_record["subjects"]:
        subject_table.insert(
            "",
            "end",
            values=(
                subject["subject_id"],
                subject["mark"],
                subject["grade"]
            )
        )#adds the student’s enrolled subjects to the table, one row per subject.

    def save_student():
        subjects = student_record["subjects"]

        total_marks = 0
        for subject in subjects:
            total_marks += subject["mark"]

        if len(subjects) > 0:
            student_record["average_mark"] = total_marks / len(subjects)

        else:
            student_record["average_mark"] = 0

        records = database.load_data()

        for record in records:
            if record["student_id"] == student_record["student_id"]:
                record.update(student_record)
                break

        database.save_data(records)

    def enrol_subject():
        if len(student_record["subjects"]) >= 4:
            messagebox.showerror(
                "Enrolment limit",
                "You can enrol in a maximum of four subjects.",
                parent=window
            )# Displays an error and returns if four subjects are already enrolled.
            return
        existing_ids = []
        for subject in student_record["subjects"]:
            existing_ids.append(subject["subject_id"])

        while True:
            new_subject = Subject()
            if new_subject.subject_id not in existing_ids:
                break

        student_record["subjects"].append(new_subject.to_dict())
        save_student()

        subject_table.insert(
            "",
            "end",
            values=(
                new_subject.subject_id,
                new_subject.mark,
                new_subject.grade
            )
        )

        count_label.configure(
            text=f"Enrolled subjects: {len(student_record['subjects'])} / 4"
        )
    def remove_subject():
        selected_items = subject_table.selection()

        if not selected_items:
            messagebox.showwarning(
                "No subject selected",
                "Please select a subject to remove.",
                parent=window
            )
            return
        
        selected_item = selected_items[0]
        subject_id = subject_table.set(selected_item, "subject_id")

        for subject in student_record["subjects"]:
            if subject["subject_id"] == subject_id:
                student_record["subjects"].remove(subject)
                save_student()

                subject_table.delete(selected_item)
                count_label.configure(
                    text=f"Enrolled subjects: {len(student_record['subjects'])} / 4"
                )
                break
    def change_password():
        password_window = tk.Toplevel(window)
        password_window.title("Change Password")
        password_window.geometry("400x300")
        password_window.configure(bg="#FFFFFF")
        password_window.transient(window)
        password_window.grab_set()

        password_form = tk.Frame(password_window, bg="#FFFFFF")
        password_form.pack(fill="both", expand=True, padx=24, pady=20)

        new_label = tk.Label(
            password_form,
            text="New password",
            bg="#FFFFFF",
            font=("Arial", 12)
        )
        new_label.pack(anchor="w")

        new_entry = tk.Entry(
            password_form,
            font=("Arial", 14)
        )
        new_entry.pack(fill="x", ipady=6, pady=(6,14))

        confirm_label = tk.Label(
            password_form,
            text="Confirm password",
            bg="#FFFFFF",
            font=("Arial", 12)
        )
        confirm_label.pack(anchor="w")

        confirm_entry = tk.Entry(
            password_form,
            font=("Arial", 14)
        )
        confirm_entry.pack(fill="x", ipady=6, pady=(6,20))

        def save_password():
            new_password = new_entry.get()
            confirm_password = confirm_entry.get()

            if not validate_password(new_password):
                messagebox.showerror(
                    "Invalid Password",
                    "The new password does not meet the required format.",
                    parent=password_window
                )
                return

            if new_password != confirm_password:
                messagebox.showerror(
                    "Password does not match",
                    "Try again.",
                    parent=password_window
                )
                return
            student_record["password"] = new_password
            save_student()

            messagebox.showinfo(
                "Password updated",
                "Your password has been changed successfully.",
                parent=password_window                
            )
            password_window.destroy()
        save_button = ttk.Button(
            password_form,
            text="Save Password",
            style="Login.TButton",
            command=save_password
        )
        save_button.pack(fill="x")
        

    button_frame = tk.Frame(content_frame, bg="#F8FAFC")
    button_frame.pack(anchor="e", pady=(20, 0))

    enrol_button = ttk.Button(
        button_frame,
        text="Enrol Subject",
        style="Login.TButton",
        command=enrol_subject,
        width=20
        #registers the function as the button’s callback. It runs when the button is clicked. 
        )
    enrol_button.pack(side="left", padx=(0, 12))

    remove_button = ttk.Button(
        button_frame,
        text="Remove Subject",
        style="Login.TButton",
        command=remove_subject,
        width=20
    )
    remove_button.pack(side="left")

    change_password_button = ttk.Button(
        button_frame,
        text="Change Password",
        style="Login.TButton",
        command=change_password,
        width=20
    )
    change_password_button.pack(side="left", padx=(12, 0))