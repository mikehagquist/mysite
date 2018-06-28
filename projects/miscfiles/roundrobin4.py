from funcs import *

teams = ["Team1", "Team2", "Team3" , "Team4", "Team5"]
     #, "Team6", "Team7", "Team8",  "Team9"] #, "Team10", 
     #"Team11", "Team12"] 

if len(teams) % 2:
    teams.append('Day off')

n = len(teams)
matchs = []
fixtures = []
count=1

for fixture in range(1, n):
    for i in range(n//2):
        matchs.append((teams[i], teams[n - 1 - i]))
    teams.insert(1, teams.pop())
    fixtures.insert(len(fixtures)//2, matchs)
    matchs = []

for fixture in fixtures:
    print ("Week ", count, fixture)
    count+=1

myweight = 185
myheight = 71
myage = 43
actlvl = 1.2

print ("BMR = " + str(get_bmr(myweight,myheight,myage)))
print ("TDEE = " + str(get_tdee(get_bmr(myweight,myheight,myage),actlvl)))
