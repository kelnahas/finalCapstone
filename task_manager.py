# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    current_task = {}

    # Split the task string by semicolon and manually add each component
    task_components = t_str.split(";")
    current_task['username'] = task_components[0]
    current_task['title'] = task_components[1]
    current_task['description'] = task_components[2]
    current_task['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    current_task['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    current_task['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(current_task)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    current_user = input("Username: ")
    current_password = input("Password: ")
    if current_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[current_user] != current_password:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


def reg_user():
    # Function to register a new user
    new_username = input("New Username: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    if new_password == confirm_password:
        if new_username in username_password:
            print("Username already exists. Please choose a different username.")
        else:
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

            print("New user added")
    else:
        print("Passwords do not match")


def add_task():
    # Function to add a new task
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    current_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": current_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            task_str = f"{t['username']};{t['title']};{t['description']};{t['due_date'].strftime(DATETIME_STRING_FORMAT)};{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if t['completed'] else 'No'}\n"
            task_list_to_write.append(task_str)
        task_file.write("".join(task_list_to_write))

    print("Task successfully added.")


def view_all():
    # Function to view all tasks
    if len(task_list) == 0:
        print("No tasks found.")
        return

    print("===== All Tasks =====")
    for index, task in enumerate(task_list, start=1):
        print(f"Task {index}:")
        print(f"Title: {task['title']}")
        print(f"Assigned to: {task['username']}")
        print(f"Date Assigned: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Task Description: {task['description']}")
        print(f"Completed: {'Yes' if task['completed'] else 'No'}")
        print()


def view_mine():
    # Function to view tasks assigned to the current user
    my_tasks = [task for task in task_list if task['username'] == current_user]

    if len(my_tasks) == 0:
        print("No tasks assigned to you.")
        return

    print("===== Your Tasks =====")
    for index, task in enumerate(my_tasks, start=1):
        print(f"Task {index}:")
        print(f"Title: {task['title']}")
        print(f"Assigned to: {task['username']}")
        print(f"Date Assigned: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Task Description: {task['description']}")
        print(f"Completed: {'Yes' if task['completed'] else 'No'}")
        print()

        print("Enter 'C' to mark the task as complete or 'E' to edit the task.")
        print("Enter 'X' to cancel and return to the main menu.")
        option = input("Option: ").upper()

        if option == 'C':
            mark_task_complete(task_list.index(task))
        elif option == 'E':
            edit_task(task_list.index(task))
        elif option == 'X':
            print("Returning to the main menu.")
            break
        else:
            print("Invalid Choice. Returning to the main menu.")


def mark_task_complete(task_index):
    # Function to mark a task as complete
    task = task_list[task_index]
    if task['completed']:
        print("Task is already marked as complete.")
        return

    task['completed'] = True
    print("Task marked as complete.")


def edit_task(task_index):
    # Function to edit a task
    task = task_list[task_index]
    if task['completed']:
        print("Cannot edit a completed task.")
        return

    print(f"Task {task_index + 1}:")
    print(f"Title: {task['title']}")
    print(f"Assigned to: {task['username']}")
    print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
    print()

    print("Enter 'U' to update the username or 'D' to update the due date.")
    print("Enter 'X' to cancel and return to the main menu.")
    option = input("Option: ").upper()

    if option == 'U':
        new_username = input("Enter new username: ")
        task['username'] = new_username
        print("Task username updated.")
    elif option == 'D':
        while True:
            try:
                new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                print("Task due date updated.")
                break
            except ValueError:
                print("Invalid datetime format. Please use the format specified.")
    elif option == 'X':
        print("Task edit canceled.")
    else:
        print("Invalid Choice. Task edit canceled.")


def generate_reports():
    # Function to generate reports
    generate_task_report()
    generate_user_report()


def generate_task_report():
    # Generate task overview report
    total_tasks = len(task_list)
    if total_tasks == 0:
        print("No tasks have been assigned, so no reports are generated.")
        return

    completed_tasks = sum(task['completed'] for task in task_list)
    incomplete_tasks = total_tasks - completed_tasks

    task_report_content = "===== Task Overview =====\n"
    task_report_content += f"Total Tasks: {total_tasks}\n"
    task_report_content += f"Completed Tasks: {completed_tasks}\n"
    task_report_content += f"Incomplete Tasks: {incomplete_tasks}\n"

    overdue_tasks = sum(
        task['due_date'].date() < date.today() and not task['completed']
        for task in task_list
    )
    incomplete_percentage = (incomplete_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / incomplete_tasks) * 100 if incomplete_tasks > 0 else 0

    task_report_content += f"Overdue Tasks: {overdue_tasks}\n"
    task_report_content += f"Percentage of Incomplete Tasks: {incomplete_percentage:.2f}%\n"
    task_report_content += f"Percentage of Overdue Tasks: {overdue_percentage:.2f}%\n"

    with open("task_overview.txt", "w") as task_report_file:
        task_report_file.write(task_report_content)

    print("Task overview report has been generated successfully.")
    print("Report file: task_overview.txt")


def generate_user_report():
    # Generate user overview report
    num_users = len(username_password)
    user_total_tasks = len(task_list)

    if user_total_tasks == 0:
        print("No tasks have been assigned to any users, so no reports are generated.")
        return

    user_report_content = "===== User Overview =====\n"
    user_report_content += f"Total Users: {num_users}\n"
    user_report_content += f"Total Tasks: {user_total_tasks}\n\n"

    for username in username_password:
        user_tasks = [task for task in task_list if task['username'] == username]
        user_assigned_tasks = len(user_tasks)
        if user_assigned_tasks == 0:
            continue
        user_completed_tasks = sum(task['completed'] for task in user_tasks)
        user_incomplete_tasks = user_assigned_tasks - user_completed_tasks
        user_overdue_tasks = sum(
            task['due_date'].date() < date.today() and not task['completed']
            for task in user_tasks
        )

        user_assigned_percentage = (user_assigned_tasks / user_total_tasks) * 100
        user_completed_percentage = (user_completed_tasks / user_assigned_tasks) * 100
        user_incomplete_percentage = (user_incomplete_tasks / user_assigned_tasks) * 100
        user_overdue_percentage = (user_overdue_tasks / user_incomplete_tasks) * 100 if user_incomplete_tasks > 0 else 0

        user_report_content += f"Username: {username}\n"
        user_report_content += f"Total Assigned Tasks: {user_assigned_tasks}\n"
        user_report_content += f"Percentage of Assigned Tasks: {user_assigned_percentage:.2f}%\n"
        user_report_content += f"Percentage of Completed Tasks: {user_completed_percentage:.2f}%\n"
        user_report_content += f"Percentage of Incomplete Tasks: {user_incomplete_percentage:.2f}%\n"
        user_report_content += f"Percentage of Overdue Tasks: {user_overdue_percentage:.2f}%\n\n"

    with open("user_overview.txt", "w") as user_report_file:
        user_report_file.write(user_report_content)

    print("User overview report has been generated successfully.")
    print("Report file: user_overview.txt")


def display_statistics():
    # Function to display task statistics
    total_tasks = len(task_list)
    completed_tasks = sum(task['completed'] for task in task_list)
    incomplete_tasks = total_tasks - completed_tasks

    print("===== Statistics =====")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Incomplete Tasks: {incomplete_tasks}")

    if incomplete_tasks > 0:
        overdue_tasks = sum(
            task['due_date'].date() < date.today() and not task['completed']
            for task in task_list
        )
        incomplete_percentage = (incomplete_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / incomplete_tasks) * 100 if incomplete_tasks > 0 else 0

        print(f"Overdue Tasks: {overdue_tasks}")
        print(f"Percentage of Incomplete Tasks: {incomplete_percentage:.2f}%")
        print(f"Percentage of Overdue Tasks: {overdue_percentage:.2f}%")

# Main program loop
while True:
    print("TASK MANAGEMENT MENU")
    print("Enter 'R' to register a user")
    print("Enter 'A' to add a task")
    print("Enter 'VA' to view all tasks")
    print("Enter 'VM' to view my tasks")
    print("Enter 'DS' to display task statistics")
    print("Enter 'GR' to generate reports")
    print("Enter 'X' to exit")

    option = input("Option: ").upper()

    if option == 'R':
        reg_user()
    elif option == 'A':
        add_task()
    elif option == 'VA':
        view_all()
    elif option == 'VM':
        view_mine()
    elif option == 'DS':
        display_statistics()
    elif option == 'GR':
        generate_reports()
    elif option == 'X':
        break
    else:
        print("Invalid Choice. Please try again.")

print("Goodbye!")
