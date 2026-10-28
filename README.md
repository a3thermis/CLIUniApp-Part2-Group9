# CLIUniApp-Part2-Group9
32555 Fundamentals of Software Development — Assessment 1 Part 2
University Application System (CLIUniApp + GUIUniApp), built in Python.

## Team
- [Ruoqi Zhou]  University System, Student System, GUIUniApp
- [Marlina Boules]  Subject Enrolment System
- [Bolorchuluun Nekhiit]  Admin System

## Requirements
- Python 3 with Tkinter support
- The GUI has been tested on macOS.

## Project Structure
```text
CLIUniApp-Part2-Group9/
├── README.md
├── students.data
├── cli/
│   ├── university_system.py
│   ├── student_system.py
│   ├── subject_enrolment_system.py
│   ├── admin_system.py
│   ├── student.py
│   ├── subject.py
│   └── database.py
└── gui/
    ├── login_window.py
    ├── Enrolment_window.py
    └── Subject_window.py
```    
Student records are stored in `students.data` in JSON format.
The file is created automatically if it does not exist.
Both the CLI and GUI use the same data file.

## How to Run
Run the following commands from the project root directory.
### Start the CLI
```bash
python cli/university_system.py
```
## Start the GUI
```bash
python gui/login_window.py
```
Start the GUI through `login_window.py`.
The other GUI modules are opened by the application.

## First-Time Use

1. Start the CLI.
2. Select `S` to enter the Student System.
3. Select `r` to register a student account.
4. Exit the CLI and start the GUI.
5. Sign in using the registered email address and password.

## GUI design
[View the GUI design in Figma]
https://www.figma.com/design/De9fqw0JmjgYMpQ4hkxtg9/CLIUniApp-GUI?node-id=1-4&t=HqSu9b8BPR9yYk4j-1
