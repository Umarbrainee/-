number_of_tasks = input("How many tasks need to be done: ")
if int(number_of_tasks) > 3:
    print("Only Three tasks included") 
tasks = ["Playing Cricket", "Watching Anime","Gaming"]
for actual_tasks in number_of_tasks:
    tasks = tasks[0:int(actual_tasks)]
    print("Please perform these tasks: " + str(tasks)) 
for x in tasks:
    tasks_to_be_done = input("Which task have you cpompleted: ")
    tasks_to_be_done = tasks_to_be_done.lower()
    if tasks_to_be_done == "playing cricket":
        tasks_left = tasks.remove("Playing Cricket")
        print("These tasks are left: "+str(tasks))
    if tasks_to_be_done == "watching anime":
        tasks_left = tasks.remove("Watching Anime")
        print("These tasks are left: "+str(tasks))
    if tasks_to_be_done == "gaming":
        tasks_left = tasks.remove("Gaming")
        print("These tasks are left: "+str(tasks))
    else:
        print("Please check the spelling of the words")
