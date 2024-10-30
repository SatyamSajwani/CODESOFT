

task=[]   #this is black task 
def add_task():
    total_task=int(input("enter the number of the task :-"))
    for i in range (1,total_task+1):
                    task_name=input(f"enter the name of {i} task is :-")
                    task.append(task_name)
    print("your task are ::- \n " )
    print("|" .join(task) )
    
            
                    # option 2 for add task in the  todo list
                    # add=(input("enter the tasks do you want to add"))
                    # task.append(add)
                    # print(f"task {add} is successfully added")      

    
def update_task():

    update=(input("enter the task do you want to update:- "))
    if update in task:
        updation=(input("enter the updated task:- "))
        ind=task.index(update)
        task[ind]=updation
        print("your task is updated successfully")
    else:
        print("the task in does't exist to update")



def delete_task():
    delete=input("enter the name of the task do you want to delete:- ")
    if delete in task:
        task.remove(delete)
        print("your task is successfully deleted ")
    else:
        print("the task in does't exsiste to delete")

def view_task():

    for i in task:
        for i,taask in enumerate(task,1):
             print(f"{i}.{taask}")
             
        print("|" .join(task))




while(True):
        op=(int(input('''
||||||||||||||||||||||-WELCOME TO TODOLIST-||||||||||||||||||||||
                enter 1 to add
                enter 2 to  update
                enter 3 to delete
                enter 4 to view
                enter 5 to exit\n Enter your Choice :- ''')))
        if op==1:
            add_task()
        elif op==2:
            update_task()
        elif op==3:
            delete_task()
        elif op==4:
            view_task()        
        elif op==5:
                print("|||||| THANK YOU FOR CHOOSEING US |||||||")
                break
        else:
            print("INVALID CHOISE ")




                    

