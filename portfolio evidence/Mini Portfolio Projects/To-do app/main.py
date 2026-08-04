##Mini Portfolio project - To-Do App
import json
import os

# ---------------Welcome Screen------------------------

def welcome_screen():
    print("""
    ==========================================
               TO-DO APP
    ==========================================

    Welcome!

    Organize your daily tasks efficiently.
    Version : 1.0 (Console MVP)

    ------------------------------------------
    Loading application...

    """)

welcome_screen()    

#-------------welcome secreen end---------------------



def menu():

    print("""
    ==============================
               MAIN MENU
    ==============================
    
    1. Add Task
    2. View Tasks
    3. Update Task
    4. Delete Task
    5. Update Task Status
    6. Search Tasks
    7. Filter Tasks
    0. Exit
    
    Select an option:
   
    """)


task_list=[]   

def save_tasks():

    print(os.getcwd())

    with open("tasks.json", "w") as file:

        json.dump(task_list, file, indent=4)

    print("Tasks Saved!")


def display_task(index, task):

    print("-" * 40)
    print(f"Task {index}")

    print(f"Title       : {task['Title']}")
    print(f"Description : {task['Description']}")
    print(f"Priority    : {task['Priority']}")
    print(f"Status      : {task['Status']}")

    print("-" * 40)

def add_task():
    print("-"*40)
    print("Add Tasks")
    print("-"*40)

    title=input("Title:")
    description=input("Description:")
    priority=input("Priority [Highest/Medium/Low]:")  

    task={
        "Title":title,
        "Description":description,
        "Priority":priority,
        "Status":"Pending"
    }

    task_list.append(task)
    #print(task_list)

    save_tasks()

    print("\n✅ Task Added Successfully!")
    print("-"*40)

def view_tasks():
    print("-"*40)
    print("View Tasks")
    print("-"*40)

    if len(task_list)==0:
        print("No Task available")
        print("-"*40)

        return

    for index,task in enumerate(task_list ,start=1):

        display_task(index, task)

        print("-" * 40)

def update_task():

    print("-" * 40)
    print("UPDATE TASK")
    print("-" * 40)

    if len(task_list) == 0:
        print("No tasks available.")
        print("-" * 40)
        return
    
    view_tasks()

    try:

        task_number = int(input("Enter Task Number: "))

        if task_number < 1 or task_number > len(task_list):
            print("Invalid Task Number")
            print("-" * 40)
            return

        task = task_list[task_number - 1]

        task["Title"] = input("New Title: ")
        task["Description"] = input("New Description: ")
        task["Priority"] = input("New Priority: ")

        save_tasks()

        print("✅ Task Updated Successfully!")

    except ValueError:
        print("Please enter a valid number.")

    print("-" * 40)


def delete_task():
    print("-"*40)
    print("Delete Tasks")
    print("-"*40)

    if len(task_list)==0:
        print("No task available.")
        print("-" * 40)
        return

    view_tasks()

    try:

        task_number=int(input("Enter Task number to delete:"))

        if task_number < 1 or task_number >len(task_list):
            print("Invalid task number.")
            print("-" * 40)
            return

        task_list.pop(task_number-1)

        save_tasks()

        print("Task Deleted Successfully!")
         

    except ValueError:
        print("Please enter a valid number")

    print("-" * 40)



def update_task_status():
    print("-"*40)
    print("Update Task Status")   
    print("-"*40)

    if len(task_list)==0:
            print("No task available.")
            print("-" * 40)
            return
    
    view_tasks()

    try:

        task_number=int(input("Enter the task number:"))

        if task_number <1 or task_number >len(task_list):
            print("Invalid task number.")
            print("-" * 40)
            return

        print("""
        1. Pending
        2. In Progress
        3. Completed
        """)

        choice=input("Choose Status:")

        if choice == "1":
            task_list[task_number - 1]['Status']="Pending"

        elif choice == "2":
            task_list[task_number - 1]['Status']="In Progress"

        elif choice == "3":
            task_list[task_number - 1]['Status']="Completed"  

        else:
            print("Invalid choice.")  
            return

        save_tasks()

        print("Status Updated Successfully!")


    except ValueError:
        print("Please enter a valid number.")

    print("-" * 40)


def search_task():
    print("-"*40)
    print("Search Task")   
    print("-"*40) 

    if len(task_list) == 0:
        print("No tasks available.")
        print("-" * 40)
        return

    keyword=input("Enter title to search: ").title()

    found=False
    
    for index , task in enumerate(task_list ,start=1):

        if keyword in task["Title"].title():

            found=True

            display_task(index, task)
            print("-" * 40)

        if not found:
            print("No matching task found.")   
            print("-" * 40)


def filter_task():

    while True:

        print("-" * 40)
        print("FILTER TASKS")
        print("-" * 40)

        print("""
1. Filter by Status
2. Filter by Priority
0. Back to Main Menu
""")

        choice = input("Enter your choice: ")

        if choice == "1":

            filter_by_status()

        elif choice == "2":

            filter_by_priority()

        elif choice == "0":

            break

        else:

            print("Invalid Choice!")
            print("-" * 40)

def filter_by_status():

    print("-" * 40)
    print("FILTER BY STATUS")
    print("-" * 40)

    if len(task_list) == 0:

        print("No tasks available.")
        print("-" * 40)
        return

    print("""
1. Pending
2. In Progress
3. Completed
""")

    choice = input("Select Status: ")

    if choice == "1":

        status = "Pending"

    elif choice == "2":

        status = "In Progress"

    elif choice == "3":

        status = "Completed"

    else:

        print("Invalid Choice!")
        print("-" * 40)
        return

    found = False

    for index, task in enumerate(task_list, start=1):

        if task["Status"] == status:

            found = True
            display_task(index, task)

    if not found:

        print(f"No {status} tasks found.")
        print("-" * 40)

def filter_by_priority():

    print("-" * 40)
    print("FILTER BY PRIORITY")
    print("-" * 40)

    if len(task_list) == 0:

        print("No tasks available.")
        print("-" * 40)
        return

    print("""
1. High
2. Medium
3. Low
""")

    choice = input("Select Priority: ")

    if choice == "1":

        priority = "High"

    elif choice == "2":

        priority = "Medium"

    elif choice == "3":

        priority = "Low"

    else:

        print("Invalid Choice!")
        print("-" * 40)
        return

    found = False

    for index, task in enumerate(task_list, start=1):

        if task["Priority"] == priority:

            found = True
            display_task(index, task)

    if not found:

        print(f"No {priority} priority tasks found.")
        print("-" * 40)                    

def exit_application():
    print("-"*40)
    print("""
    
    Thank you for using To-Do App!
    
    Goodbye!
    
    """)    
 


##----------------Menu-------------


while True:

    menu()
     
    try:


        menu_choice=int(input(" Enter a Number from menu [0-7]:"))
        print(f"You entered: {menu_choice}")

        if menu_choice==1:
            add_task()
            

        elif menu_choice==2:
            view_tasks()
            

        elif menu_choice==3:
            update_task()
            

        elif menu_choice==4:
            delete_task()
           

        elif menu_choice==5:
            update_task_status()
          

        elif menu_choice==6:
            search_task()
            

        elif menu_choice==7:
            filter_task()
            

        elif menu_choice==0:
            exit_application()
            break

        else:
            print("Invalid Input enter a correct option ")    
            print("-"*40)              

    except ValueError:
        
        print("Please enter a valid Number from menu [0-7]")
        print("-"*40)
        continue









