from tasks import task
from datetime import date

class user:
    #counters for failed/ successfully finished tasks. A task is considered failed when it's not done in time
    #if someone fails a task a new deadline is automatically assigned adding 25% of the initial time

    fail_counter = 0
    success_counter = 0

    # task vector to store all of the tasks associated with the user    
    task_list = []

    # a variable to store the user's points gained over time
    points = 0

    # user's first name 
    first_name = None
    
    # user's last name
    last_name = None

    # username -- must be unique, can be chosen by the user
    username = None    
    
    # password -- user's password for login
    password = None

    # users can be part of a clan to see clan member's private stats and compete
    # with close friends 
    clan_tag = None#de facut fail succ counter
#la update points


    # basic constructor
    def __init__(self, first_name, last_name, password, clan_tag, username):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.clan_tag = clan_tag
        self.username = username

    # for debugging, prints everyting
    def printvars(self):
        print(self.first_name, self.last_name, self.password, self.clan_tag, self.username)
    
    # gets a task object and gets the points from its finishTask method
    def updatePoints(self, val: task):
        self.points += task.finishTask(val)
    
    # the more recent tasks are inserted at the beginning 
    # task vector
    def addTask(self, task):
        self.task_list.insert(0, task)

    # when finishing a task we add 1 to the success counter and also remove the task 
    # from the user's task_list
    def removeTask(self, task):
        # don't forget to add points when finnishing a task
        # self.updatePoints(task.pointGain)
        self.updatePoints(task)
        self.task_list.remove(task)
        self.success_counter += 1



u1 = user("Mircea", "Ionescu", "parola123", "CNMV", "mircea")
u1.printvars()


t1 = task("first_task", "this is my first task", True, "Easy", date.today(), "cool")

u1.addTask(t1)

print(u1.task_list[0].title)

u1.removeTask(u1.task_list[0])
print(u1.success_counter, u1.task_list, u1.points)
