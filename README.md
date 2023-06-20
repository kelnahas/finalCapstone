# Final Capstone

## Task Management System
This task management system is a command-line interface (CLI) based application in Python. It provides an organised system for tracking, assigning, editing, and completing tasks. Users can also register, log in, and view tasks assigned to them.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)

# Installation
Follow the steps below to install and run the project locally.

1. **Clone the repository:** ```git clone https://github.com/<your_username>/finalCapstone.git```
3. **Navigate into the project directory:** ```cd finalCapstone```
4. **Ensure you have Python 3.x installed on your system:** You can check this by running: ```python --version```
5. **Run the main script:** ```python task_manager.py```

# Usage
The program is interactive and provides a menu-based interface for the user. Below is an overview of how to use the application.

1. **Login or Register**: When the program starts, you will be prompted to login (Default User: admin Password: password. If you don't have an account, you can register a new one. 

2. **The Main Menu** provides several options:
   - `R`: Register a new user
   - `A`: Add a new task
   - `VA`: View all tasks
   - `VM`: View tasks assigned to the current user
   - `DS`: Display task statistics
   - `GR`: Generate reports
   - `X`: Exit the application

Please note that all inputs for dates should follow the "YYYY-MM-DD" format.

3. **Add Task**: Adding a task requires inputting the task details including the assignee, task title, description, and due date.
4. **Viewing Tasks**: Viewing tasks shows a list of tasks with their details, including whether they are completed or not.
5. **Statistics**: The statistics option shows a summary of tasks, such as total tasks, completed, incomplete, and overdue tasks.
6. **Reports**: The reports option generates a report of all tasks and user overviews.

# Contributors
- kelnahas ([GitHub Profile](https://github.com/kelnahas))
