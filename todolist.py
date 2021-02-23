#todo_list.py
#This programme lets users to add and display tasks to complete
#Ishanika Singh. 15th Feb 2021

#Declare Varibales, Lists
name = input("What is your name?")
print("Hi", name)
print("Welcome to the To Do list programme where you can write down all of the tasks which you would like to finish today")

to_do = ["Buy Clothes", "Pay Bills", "Ring Parents"]
a = "yes"


def task():
    print("You Can Choose a maximum of three tasks")
    task = input("New Task: ")
    another_task = input("New Task: ")
    third_task = input("New Task: ")
    print("Your Tasks are the following: ")
    print(task)
    print(another_task)
    print(third_task)
    return
    
to_do.append(task)    

while "yes" in a:
    print("Choose a task by enterng the number 1, If you would like to view the list, select 2 and if you would like to exit, select 3: ")
    print("1. Add a task")
    print("2. View the List")
    print("3. Exit")
    
    number_chosen = int(input("Enter number here: "))  
    
    if number_chosen == 1:
        task()
    elif number_chosen == 2:
        print("Here is an example of a to_do list:")
        print(to_do)
    elif number_chosen == 3:
        print("Goodbye!")
    else:
        print("INVALID NUMBER")
        

        

        

    


    
    


