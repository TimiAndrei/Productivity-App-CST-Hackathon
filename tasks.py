from datetime import date, timedelta
from math import floor

class task:
    title = None
    # title of the task
    description = "Default Description"
    # description of the task
    visibility = False
    # visibility of the task(default is False aka private)
    # in case it is public, other users can see it and contribute
    difficulty = None
    # difficulty of the task(default diff is Easy)
    # based on this, you can get bonus points
    deadline = date.today() + timedelta(days = 1)
    # the deadline of the task (default is the next day)
    duration = deadline - date.today()
    #this is the set duration for the task(how long it is going to take to finish)
    task_type = "task".title()
    # task type (default is task)
    # these can be Task, Improvement or New Technology
    difficulty_bonus = {
        "Easy" : 1,
        "Medium" : 1.4,
        "Hard" : 2
    }
    # this is the point multiplier based on the difficulty of the task

    def __init__(self, title, description, visibility, difficulty, deadline, task_type):
        self.title = title
        self.description = description
        self.visibility = visibility
        self.difficulty = difficulty
        self.deadline = deadline
        self.task_type = task_type
        print("Created task " + self.title + " for user ") 

    def finishTask(self):
        points = 5
        # this is the deafault value of points per task

        points *= self.difficulty_bonus[self.difficulty]
        # multiply the points based on the difficulty

        days_to_deadline = self.deadline - date.today()
        # how many days are left until the deadline
        used_days_percentage = floor(days_to_deadline.days * 100 / self.duration.days)
        # percentage of the total duration the completion of the task took
        # based on this, a point bonus is awarded.
        
        points += points * used_days_percentage
        # adding bonus points based on how much time was left on the task

        return points

    def isExpired(self):
        # this will check if the task has extended over the deadline
        # if it is the case, it will be counted as a failed task, but the deadline will be extended by 25% of the initial duration
        if(date.today() > self.deadline):
            self.deadline += self.deadline.days() * 0.25
            print("New deadline: {}", self.deadline)
            return True
        
        return False

# Task1 = tasks("Primul task", "Hai sa adaugan si o descirere", True, "Hard", date.today(), "Task")

# print(vars(Task1))