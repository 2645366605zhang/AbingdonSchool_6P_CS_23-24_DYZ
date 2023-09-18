import os

localDirection = os.path.dirname(__file__)
relativeDirection = "txtfile/taskmanager/task_list.txt"
taskFileDirection = os.path.join(localDirection, relativeDirection)

currentTask = [-1, "No task"]
tasks = []

def menu():
    global currentTask
    global tasks
    programOn = True
    tasks = importTask(tasks)
    while programOn:
        currentTask = checkCurrentTask()
        print(f"""

┌──────────────────────┐
│Task Management System│
└──────────────────────┘

Current Task: {currentTask[1]}

1. Create a new task
2. Remove completed tasks
3. Show list of tasks
4. Show next task
5. Mark current task as complete
6. Manually import tasks
7. Export tasks
8. Quit
        """)
        try:
            menuChoice = int(input("Please enter the number of your choice."))
            if menuChoice == 1:
                createTask()
            elif menuChoice == 2:
                removeCompleted()
            elif menuChoice == 3:
                showTask()
            elif menuChoice == 4:
                nextTask()
            elif menuChoice == 5:
                completeTask()
            elif menuChoice == 6:
                importConfirmation = input('Importing tasks manually from file will completly orerride existing tasks!\nEnter "Yes" to continue.')
                if importConfirmation.upper() == "YES":
                    tasks = importTask(tasks)
                    print("Tasks imported!")
                else:
                    print("Manual import cancelled, returning to menu.")
            elif menuChoice == 7:
                exportConfirmation = input('Importing tasks manually from file will completly orerride existing tasks!\nEnter "Yes" to continue.')
                if exportConfirmation.upper() == "YES":
                    exportTask()
                else:
                    print("Export cancelled, returning to menu.")
            elif menuChoice == 8:
                programOn = False
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

def checkCurrentTask():
    currentTaskIndex = 0
    currentTaskString = "No task"
    for task in tasks:
        if task[2] == "×":
            currentTaskString = task[1]
            break
        currentTaskIndex += 1
    return [currentTaskIndex, currentTaskString]

def createTask():
    if len(tasks) > 999:
        print("Number of tasks will exceed 999 if another task is added, task creation cancelled!")
    else:
        taskDetail = input("Please enter the details of the task you want to add, leave blank to cancel.")
        if taskDetail == "":
            print("Operation cancelled!")
        else:
            tasks.append([(len(tasks) + 1), taskDetail, "×"])

def removeCompleted():
    removeConfirmation = input('This will remove all tasks that is marked completed!\nEnter "Yes" to continue.')
    if removeConfirmation.upper() == "YES":
        removeTargetList = []
        for task in tasks:
            if task[2] == "✓":
                removeTargetList.append(task[0] - 1)
        for target in sorted(removeTargetList, reverse = True):
            del tasks[target]
        newTaskIndex = 1
        for task in tasks:
            task[0] = newTaskIndex
            newTaskIndex += 1
        print("Completed tasks removed!")
    else:
        print("Operation cancelled!")

def showTask():
    print("\n\n\n")
    for task in tasks:
        print(f"{task[0]:3}. {task[1]} - {task[2]}")
    userConfirmation = input("\nPress enter to return to menu.")

def nextTask():
    print(f"\nThe next task is:\n{tasks[currentTask[0] + 1][1]}")

def completeTask():
    global currentTask
    if currentTask[1] == "No task":
        print("There are no tasks in the task list for you to mark as completed.")
    else:
        completeConfirmation = input('This will mark the current task as completed!\nEnter "No" to cancel, press enter to continue.')
        if completeConfirmation.upper() == "NO":
            print("Operation cancelled!")
        else:
            tasks[currentTask[0]][2] = "✓"
            currentTask = checkCurrentTask()
            print(f"Task {tasks[currentTask[0]][1]} is marked as completed!")

def importTask(taskList):
    try:
        taskFile = open(taskFileDirection, "r")
        taskIndex = 1
        for line in taskFile:
            dataList = line.split("|")
            taskDetail = dataList[0]
            if dataList[1] == "done\n":
                status = "✓"
            elif dataList[1] == "not done\n":
                status = "×"
            else:
                status = "Missing status data in task_list.txt! Your task_list.txt file might be corrupted."
            taskList.append([taskIndex, taskDetail, status])
            taskIndex += 1
        taskFile.close()
    except FileNotFoundError:
        print("\ntask_list.txt not found, generating a new file.\n")
        taskList = []
    return taskList

def exportTask():
    taskFile = open(taskFileDirection, "w")
    for record in tasks:
        taskFile.write(record[1])
        taskFile.write("|")
        if record[2] == "✓":
            taskFile.write("done")
        elif record[2] == "×":
            taskFile.write("not done")
        else:
            print("Status data not found in current tasks, there should be a bug causing this!")
        taskFile.write("\n")
    taskFile.close()
    print("\nTasks successfully exported!")

menu()