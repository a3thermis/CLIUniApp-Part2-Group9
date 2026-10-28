# Individual Contribution Statement
Project: CLIUniApp-Part2-Group9
Course: 32555 Fundamentals of Software Development
Assessment: Assessment 1 — Part 2


## Crystal Nekhiit 
```text
Implemented database.py and admin_system.py. Developed the database functionality for managing student records through JSON file handling, including database file path configuration, file creation when missing, loading and saving records, calculating missing average marks, and searching for students by email. Implemented the administrative functions for grade grouping, PASS/FAIL partitioning, student removal, displaying student records, and clearing the database with confirmation checks. Beyond individual implementation, tested the entire CLI application to verify that the modules worked together correctly, identified and fixed integration bugs, investigated data persistence and database file connection issues, and systematically compared the CLI prompts, input messages, output messages, spacing, and indentation against the assignment's sample output. Corrected formatting inconsistencies to improve compliance with the specified input/output requirements and the consistency of the integrated application.
```

## Ruoqi Zhou
### System Development 
I was mainly responsible for the University System, Student System, and GUIUniApp, as well as the initial frameworks and subsequent refinement of `database.py` and `student.py`. I also completed component integration, manual testing, debugging, and documentation.
In `cli/university_system.py`, I implemented a looping main menu for entering the Student System or Admin System, or exiting, with uppercase input handling and invalid-choice messages. In `cli/student_system.py`, I implemented registration and login, including email and password validation, duplicate email checks, and unique six-digit student ID generation. Registration creates a Student object, converts it with `to_dict()`, and saves it through the Database class.
The CLI and GUI share my email and password validation functions. The final password pattern is:
```python
PASSWORD_REGEX = r"[A-Z][A-Za-z]{4,}[0-9]{3,}"
```
With `re.fullmatch()`, it requires an uppercase first letter, at least five English letters in total, followed by at least three digits.
I created the Figma design draft and implemented the GUI using Tkinter and ttk. In `gui/login_window.py`, I created the main window, login form, shared button styles, and page switching. In `gui/Enrolment_window.py`, I implemented the subject table, enrolment, removal, password changes, logout, saving, and subject count updates. In `gui/Subject_window.py`, I created a separate window displaying subject IDs, marks, and grades. I used frames and layout managers for layout, callbacks for button actions, and `Toplevel` for additional windows. I added input and enrolment checks, and used the clam theme for button colours on macOS.
### Manual Testing and Bug Fixes
I manually tested my registration and login flows and the GUI workflow. The checks included valid and invalid input, login, page transitions, adding and removing subjects, the four-subject limit, viewing subjects, changing passwords, and logout. I also checked that a changed password could be used to log in.
During development, I investigated and resolved issues involving:
- **Syntax and dictionary access:** incorrect window geometry syntax, missing commas, and a misspelled password dictionary key. 
- **Imports and scope:** module search paths, undefined variables, and incorrect indentation.
- **GUI appearance and behaviour:** macOS button colours, inconsistent spacing, misaligned buttons, and a blank password window.
### Documentation and Presentation
I prepared the README, including the project overview, project structure, setup and execution instructions, and GUI design link. I also prepared my presentation and source-code walkthrough for the University System and Student System, an explanation of the Student model.