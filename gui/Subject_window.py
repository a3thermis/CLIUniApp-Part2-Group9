import tkinter as tk
from tkinter import ttk


def show_subject_window(window, student_record):
    subject_window = tk.Toplevel(window)
    subject_window.title("My Subjects")
    subject_window.geometry("800x450")
    subject_window.configure(bg="#F8FAFC")
    subject_window.transient(window)
    subject_window.grab_set()

    content_frame = tk.Frame(subject_window, bg="#F8FAFC")
    content_frame.pack(fill="both", expand=True, padx=24, pady=24)

    title_label = tk.Label(
        content_frame,
        text="My Subjects",
        bg="#F8FAFC",
        fg="#1E3A8A",
        font=("Arial", 24, "bold")
    )
    title_label.pack(anchor="w", pady=(0, 12))

    count_label = tk.Label(
        content_frame,
        text=f"Enrolled Subjects: {len(student_record['subjects'])} / 4",
        bg="#F8FAFC",
        fg="#0F172A",
        font=("Arial", 12)
    )
    count_label.pack(anchor="e", pady=(0, 12))

    subject_table = ttk.Treeview(
        content_frame,
        columns=("subject_id", "mark", "grade"),
        show="headings",
        height=6
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
    close_button = ttk.Button(
        content_frame,
        text="Close",
        style="Login.TButton",
        command=subject_window.destroy
    )
    close_button.pack(anchor="e", pady=(20, 0))