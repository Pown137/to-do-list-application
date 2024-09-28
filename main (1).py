def task_manager():
    tasks = []
    
    while True:
        action = input("\nEnter 'add' to add a task, 'edit' to edit a task, 'delete' to delete a task, 'show' to display tasks, or 'quit' to exit: ").lower()

        if action == 'add':
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")

        elif action == 'edit':
            task_index = int(input("Enter the task number to edit (starting from 1): ")) - 1
            if 0 <= task_index < len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_index] = new_task
                print("Task updated.")
            else:
                print("Invalid task number.")

        elif action == 'delete':
            task_index = int(input("Enter the task number to delete (starting from 1): ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")

        elif action == 'show':
            print("Current Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif action == 'quit':
            break

        else:
            print("Invalid action. Please try again.")

task_manager()
