tasks=[]

while True:
    print("1.add task")
    print("2.remove task")
    print("3.list tasks")
    print("4.quit")

    choice=int(input("enter your choice"))
    
    if choice==1:
        task=input("enter task")
        tasks.append(task)
    elif choice==2:
        task=input("enter task to remove")
        if task in tasks:
            tasks.remove(task)
        else:
            print("tasks is not here")
    elif choice==3:
        for i,task in enumerate(tasks):
            print(f"{i+1}. {task}.")
    elif choice==4:
        break
    else:
        print("invalid choice")
