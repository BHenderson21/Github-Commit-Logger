import os
from datetime import date
from collections import namedtuple

commitStack = []
commitStack2 = []
commitStack3 = []
commit = ""
i = 0

repoLocation = input('Enter the address of the repo you would like the log for: ')
cdCommand = 'cd ' + repoLocation
rawFile = str(date.today()) + "raw.txt"
newFile = str(date.today()) + ".txt"
os.system('cd ' + repoLocation + '&& git log > '+ rawFile)

rawLogs = open(repoLocation + "/" + rawFile, "r")
newLogs = open(repoLocation + "/" + newFile, "w")

lines = rawLogs.readlines()
for line in lines:
    if line[0:6] == "Author":
        commitStack.append(commit)
        commit = ""
        commit += line
    elif line[0:4] == "Date":
        commit += line
    elif(line[0:6] != "commit"):
        if(line[0:5] != "Merge"):
            commit += line
    elif(line[0:6] == "commit"):
        commitStack.append(commit)
        break

for line in lines:
    if line[0:6] == "Author":
        if i < 50:
            commitStack.append(commit)
        else:
            if i < 100:
                commitStack2.append(commit)
            else:
                commitStack3.append(commit)
        print(commit)
        commit = ""
        commit += line
    elif line[0:4] == "Date":
        commit += line
    elif(line[0:6] != "commit"):
        if(line[0:5] != "Merge"):
            commit += line
    i += 1

for i in commitStack3:
    newLogs.write(commitStack3.pop())
for i in commitStack2:
    newLogs.write(commitStack2.pop())
for i in commitStack:
    newLogs.write(commitStack.pop())

