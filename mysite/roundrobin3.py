
# def tourney(teams):
teams = ["Team1", "Team2", "Team3", "Team4", "Team5",
     "Team6", "Team7", "Team8", "Team9",  "Team10", 
     "Team11", "Team12"] #, "Team13"]
#teams = ["Team1", "Team2", "Team3", "**Blind**"]

if len(teams) % 2:
    teams.append('**BLIND**')

n = len(teams)
matchs = []
fixtures = []
count=1

for fixture in range(1, n):
    for i in range(n // 2): #floor of number of teams divided by 2
        #print("loop {} times" .format(n))
        #print("Loop ", n, " times.")
        matchs.append((teams[i], teams[n - 1 - i]))
        #print (teams[i], teams[n - 1 - i])
    teams.insert(1, teams.pop())
    fixtures.insert(len(fixtures) // 2, matchs)
    matchs = []

#print (fixtures)
for item in fixtures:
    print ("Week ", count, item)
    count+=1


# teams2 = ["Team1", "Team2", "Team3", "Team4", "Team5", "**BLIND**"]
# print (teams2)
# teams2.insert(1, teams2.pop())
# print (teams2)
# teams2.insert(1, teams2.pop())
# print (teams2)
# good = []
# crap = [1, 2, 3]
# good.insert(0, crap.pop())
# good.insert(1, crap.pop())
# print ("crap is", crap)
# print ("good is", good)

