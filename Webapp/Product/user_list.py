from user import user
from tasks import task
from datetime import date

class userList:
    users = []

    # appends at the end of the list a new user entry
    def addUser(self, first_name, last_name, password, clan_tag, username):
        self.users.append(user(first_name=first_name, last_name=last_name, password=password, clan_tag=clan_tag, username=username))

    # self explanatory, quite useful function especially since username is supposed to be unique
    def getUserFromUsername(self, username):
        for i in self.users:
            if i.username == username:
                return i  

    # looks for an object having a specific username and deletes the user in question
    def rmUser(self, username):
        self.users.remove(self.getUserFromUsername(username))    

    # sorts users and returns a list of size 5% of the wanted size
    def getTop5(self):
        self.users.sort(key=lambda user: user.points, reverse=True)
        
        #var to store the top 25%  
        not_zero_aux = int(5/100 * len(self.users))

        #on small input you still want someone in the top % so it's never 0
        if not_zero_aux == 0:   
            not_zero_aux += 1
            
        # return the top % slice of users
        return self.users[0:not_zero_aux] 
        

    def getTop10(self):
        self.users.sort(key=lambda user: user.points, reverse=True)
        not_zero_aux = int(10/100 * len(self.users))

        if not_zero_aux == 0:
            not_zero_aux += 1
            
        return self.users[0:not_zero_aux] 
        

    def getTop15(self):
        self.users.sort(key=lambda user: user.points, reverse=True)
        not_zero_aux = int(15/100 * len(self.users))

        if not_zero_aux == 0:
            not_zero_aux += 1
            
        return self.users[0:not_zero_aux] 
        
    def getTop25(self):
        self.users.sort(key=lambda user: user.points, reverse=True)
        not_zero_aux = int(25/100 * len(self.users))

        if not_zero_aux == 0:
            not_zero_aux += 1
            
        return self.users[0:not_zero_aux] 
        
    # returns an integer with the bracket corresponding to the given username
    def getUserBracket(self, username):
        # humans work with usernames, computers work with objects
        the_user = self.getUserFromUsername(username)
        if the_user in self.getTop5():
            return int(5)
        elif the_user in self.getTop10():
            return int(10)
        elif the_user in self.getTop15():
            return int(15)
        elif the_user in self.getTop25():
            return int(25)
        else:
            return 100
             
    def getClan(self, clan_tag):
        clan_users = []
        for i in self.users:
            if i.clan_tag == clan_tag:
                clan_users.append(i)
        
        clan_users.sort(key=lambda user: user.points, reverse=True)

        return clan_users
    

l = userList()
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "User0")
l.addUser("Ioan", "Alexandru", "parola123", "CNMV", "User1")
l.addUser("Andrei", "Timotei", "parola123", "CNMV", "User2")
l.addUser("Drăgan", "Mihăiță", "ciscoenapa55", "CNMV1", "User3")
l.addUser("Marciu", "Andrei", "parola123", "CNMV", "User4")
l.addUser("Dobrovat", "Poo", "parola123", "CNMV", "User5")
l.addUser("Ana", "Uban", "parola123", "CNMV", "User6")
l.addUser("Mihai", "Bratu", "parola123", "CNMV", "User7")
l.addUser("Ioana", "Musat", "parola123", "CNMV", "User8")


# l.addUser("Mircea", "Ionescu", "parola123", "CNMV2", "U8")
# l.addUser("Mircea", "Ionescu", "parola123", "CNMV3", "U9")
# l.addUser("Mircea", "Ionescu", "parola123", "CNMV4", "U10")
# l.addUser("Mircea", "Ionescu", "parola123", "CNMV4", "U11")
# l.addUser("Mircea", "Ionescu", "parola123", "CNMV5", "U12")
# l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U13")
# l.addUser("Mircea", "Ionescu", "parola123", "CNMV5", "U14")
# l.addUser("Mircea", "Ionescu", "parola123", "CNMV5", "U15")

l.users[0].points = 90
l.users[0].addTask(task("Primul task", "Hai sa adaugam si o descirere", True, "Hard", date.today(), "Task"))
l.users[1].points = 20
l.users[2].points = 5
l.users[3].points = 15
l.users[3].addTask(task("Primul task", "Hai sa adaugam si o descirere", True, "Easy", date.today(), "Task"))
l.users[1].current_streak=3
l.users[0].max_streak=5
l.users[0].current_streak=3
l.users[0].badges["Improvements"]=3
l.users[0].badges["New Technology"]=1
# l.users[4].points = 110
# l.users[5].points = 24
# l.users[6].points = 51
# l.users[7].points = 35

# l.users[8].points = 11
# l.users[9].points = 23
# l.users[10].points = 51
# l.users[11].points = 65
# l.users[12].points = 80
# l.users[13].points = 41
# l.users[14].points = 59
# l.users[15].points = 74

# print(l.users)

# print(l.getClan("CNMV"))