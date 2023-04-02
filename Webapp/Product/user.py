from tasks import task
from datetime import date, timedelta
from retrieve_data import *

class user:
    #counters for failed/ successfully finished tasks. A task is considered failed when it's not done in time
    #if someone fails a task a new deadline is automatically assigned adding 25% of the initial time

    fail_counter = 0
    success_counter = 0
    task_counter = 0
    # the number of tasks the user has had
    # this will be used for the index of the tasks

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

    
    improvement_counter = 0
    # this is a counter of the number of "Improvement" tasks that have been completed
    # we will use this for giving out badges
    new_tech_counter = 0
    # this is a counter of the number of "New Technology" tasks that have been completed
    # we will use this for giving out badges
    last_finish_date = date.today() - timedelta(days = 2)
    # this marks the day of the last task finished
    # this will be used for assigning streaks
    # by default, this is set to two days before the creation of the account, so as not to interfere with the rules
    current_streak = 0
    # this is the counter for the current streak
    # this is set to 0, as default
    max_streak = 0
    # this will be used to mark the largest streak the user has acheived

    badges = {
        "Improvements" : 0,
        "New Technology" : 0
    }

    # basic constructor
    def __init__(self, first_name, last_name, password, clan_tag, username):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.clan_tag = clan_tag
        self.username = username

        addUser(username, password, first_name, last_name, clan_tag, self.points, self.fail_counter, self.success_counter)

    def __repr__(self):
        return self.username + " " + str(self.points)

    # for debugging, prints everyting
    def printvars(self):
        print(self.first_name, self.last_name, self.password, self.clan_tag, self.username)
    
    # gets a task object and gets the points from its finishTask method
    def finishTask(self, val: task):
        plus, task_type = task.finishTask(val)
        #gets the points that should be added to the total tally and gets the type of the finished task

        # print(task_type)

        self.points += plus
        #adds the points earned for the completion

        if task_type == "Improvement":
            self.improvement_counter += 1
        if task_type == "New Technology":
            self.new_tech_counter += 1
        # depending on the task type, the counter for the respective category gets incremented

        if self.improvement_counter == 3:
            self.badges["Improvements"] += 1
            self.improvement_counter = 0

        if self.new_tech_counter == 3:
            self.badges["New Technology"] += 1
            self.new_tech_counter = 0
        # for three tasks of these two types, the user gets a badge for them

        finish_time_diff = (date.today() - self.last_finish_date).days
        # this is the time difference between the current finished task and the one before
        # if this difference is 1, then the last finished task was yesterday, and the streak can get inceremented
        # this also means that we can update the finish_date with today.
        if finish_time_diff == 1:
            self.current_streak += 1
            self.last_finish_date = date.today()
            if self.current_streak > self.max_streak:
                self.max_streak = self.current_streak

        # however, if the time difference is greater that 1, we will break the streak and set the last finished task to today
        elif finish_time_diff > 1:
            self.current_streak = 0
            self.last_finish_date = date.today()

        # print(self.current_streak)


        # print(self.new_tech_counter)


    
    # the more recent tasks are inserted at the beginning 
    # task vector
    def addTask(self, task):
        self.task_list.insert(0, task)
        date_string = task.deadline.strftime("%m/%d/%Y")

        duration = task.deadline - date.today()

        addTasks(str(self.task_id), task.title, task.description, task.difficulty, "to_date({date}, 'DD-MM-YYYY')".format(date = date_string), "to_date({days}, 'DD')".format(days=duration.days), task.task_type, self.username)

    # when finishing a task we add 1 to the success counter and also remove the task 
    # from the user's task_list
    def removeTask(self, task):
        # don't forget to add points when finnishing a task
        # self.updatePoints(task.pointGain)
        self.finishTask(task)
        self.task_list.remove(task)
        self.success_counter += 1


#for testing purposes below 

u1 = user("Mircea", "Ionescu", "parola123", "CNMV", "mircea")
u1.printvars()


t1 = task("first_task", "this is my first task", True, "Medium", date.today(), "New Technology")

u1.addTask(t1)

print(u1.task_list[0].title)

u1.removeTask(u1.task_list[0])
print(u1.success_counter, u1.task_list, u1.points)
