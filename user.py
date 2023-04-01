# import from tasks tasks
# de aici voi avea o lista de taskuri

class user:
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
    clan_tag = None

    def __init__(self, first_name, last_name, password, clan_tag, username):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.clan_tag = clan_tag
        self.username = username


    def printvars(self):
        print(self.first_name, self.last_name, self.password, self.clan_tag, self.username)
    
    
    def updatePoints(self, value):
        self.points += value
    
    # the more recent tasks are inserted at the beginning 
    def addTask(self, task):
        self.task_list.insert(0, task)

    def removeTask(self, task):
        # don't forget to add points when finnishing a task
        # self.updatePoints(task.pointGain)
        self.task_list.remove(task)



u1 = user("Mircea", "Ionescu", "parola123", "CNMV", "mircea")
u1.printvars()

u1.updatePoints(100)
u1.updatePoints(300)
print(u1.points)
