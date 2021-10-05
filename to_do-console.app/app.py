#To-do console app

id = 0
myList = []

job_1 = {
    "job": "Read book",
    "flag": "Not performed"
}
job_2= {
    "job": "Play on game",
    "flag": "Not performed"
}
job_3 = {
    "job": "Make exercise",
    "flag": "Not performed"
}
myList.append(job_1)
myList.append(job_2)
myList.append(job_3)




def addToList(job):
    data = {
        "job": job,
        "flag": "Not performed"
    }
    myList.append(data)

def headUI():
    print('===============================================================')
    print('Job name                              | Status')
    print('---------------------------------------------------------------')

def showAllJobs(list):
    headUI()
    job = "job"
    flag = "flag"
    index = 0
    for item in list:
        print(f"{index} {item[job]}                                | {item[flag]}")
        index += 1

def removeJob(index):
    myList.pop(index)

def changeJobStatus(index):
    flag = "flag"
    job = "job"
    headUI()
    print(f" {myList[index][job]}   | {myList[index][flag]}")
    print('-------------------------------------------------')
    status = input(f"Enter status: \n"
                   f"1 - Done \n"
                   f"2 - Not performed")
    if status == '1':
        myList[index][flag] = "Done"
    if status == '2':
        myList[index][flag] = "Not performed"
    headUI()
    print(f" {myList[index][job]}   | {myList[index][flag]}")

def controlKey(key):
    if key == "1":
        #add new job
        job = input('Enter new job: ')
        addToList(job)
    if key == "2":
        number = input('Remove job \n Enter job number: ')
        removeJob(int(number))
    if key == "3":
        showAllJobs(myList)
    if key == "4":
        number = input('Change job status \n Enter job number')
        changeJobStatus(int(number))


def uiRender():
    print('----------------------------')
    print(f'Key 1 - add new job \n'
          f'Key 2 - remove job \n'
          f'Key 3 - show all jobs \n'
          f'Key 4 - change job status \n'
          f'Key q - exit')

def app():
    key = "a"
    while key != "q":
        uiRender()
        key = input(f'Enter your key: ')
        controlKey(key)


app()










