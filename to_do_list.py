def Task():
    tasks = []#empty list
    total_task=int(input("enter no.of tasks"))
    for i in range(1,total_task+1):
        task_name=input(f"enter task{i}:")
        tasks.append(task_name)
    print(f"todays tasks are:\n{tasks}")
    while True:
        operation=int(input("enter your choice:\n1-add\n2-update\n3-delete\n4-view\n5-stop\exit"))
        if operation==1:
            add_task=input("enter the task to add")
            tasks.append(add_task)
            print("task added successfully") 
        elif operation==2:
            update_task=input("name the task you want to update")
            if update_task in tasks:
                update=input("enter the new task")
                index=tasks.index(update_task)
                tasks[index]=index
                print("task has updated")
        elif operation==3:
            del_task=input("name the task you want to delete")
            if del_task in tasks:
                ind=tasks.index(del_task)
                del tasks[ind]
                print("task is deleted")
        elif operation==4:
            print("following are the task:")
            print(tasks)
        elif operation==5:
            print("program has ended")
            break
        else:
            print("invalid input")
Task()

