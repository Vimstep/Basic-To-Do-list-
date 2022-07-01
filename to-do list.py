
tasks = {}


while True:
    print("Pick Option:\n New Task:1 \n Delete Task:2 \n Print Tasks:3")
    answer = int(input())

    def new_task(list):
        print("Input Name of task *WARNING you title needs to be under 50 characters*")
        answer = input()

        while len(answer) > 50:
            print("Error to many characters")
            answer = input()
            if answer is "" or answer is " ":
                print("Just add a character")
    
        print("So what would you like to add?")
        answer2 = input()
        list[answer] = answer2
    

    def delete_task(list):
        print("Which one do you like to delete?")

        if len(list) == 0:
            print("Sorry You have no tasks")
    
        for i in range(len(list)):
            print("*"+str(list.keys()))
            answer = input()
            if answer in list:
                list.clear()    

    def print_tasks(list):
        print("Whould you like to see content")
        for i in range(len(list)):
            print("*"+str(list.keys()))
            answer = input()
            if answer in list:
                print(list[answer])



    if answer == 1:
        new_task(tasks)
    elif answer == 2:
        delete_task(tasks)
    elif answer == 3:
        print_tasks(tasks)
