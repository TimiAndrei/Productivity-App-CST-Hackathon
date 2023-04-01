from user import user
from tasks import task

class userList:
    users = []

    # appends at the end of the list a new user entry
    def addUser(self, first_name, last_name, password, clan_tag, username):
        self.users.append(user(first_name=first_name, last_name=last_name, password=password, clan_tag=clan_tag, username=username))

    # looks for an object having a specific username and deletes the user in question
    def rmUser(self, username):
        for i in self.users:
            if i.username == username:
                self.users.remove(i)

    # sorts users and returns a list of size 5% of the wanted size
    def getTop5(self):
        self.users.sort(key=lambda user: user.points, reverse=True)
        
        #var to store the top 25%  
        not_zero_aux = int(25/100 * len(self.users))

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
        


l = userList()
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U0")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U1")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U2")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U3")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U4")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U5")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U6")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U7")

l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U8")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U9")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U10")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U11")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U12")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U13")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U14")
l.addUser("Mircea", "Ionescu", "parola123", "CNMV", "U15")


l.users[0].points = 10
l.users[1].points = 20
l.users[2].points = 5
l.users[3].points = 15
l.users[4].points = 110
l.users[5].points = 24
l.users[6].points = 51
l.users[7].points = 35

l.users[8].points = 11
l.users[9].points = 23
l.users[10].points = 51
l.users[11].points = 65
l.users[12].points = 80
l.users[13].points = 41
l.users[14].points = 59
l.users[15].points = 74


print(l.users)

print(l.getTop15())
