# Importing Modules
import csv
import bullet
import os
from pyfiglet import Figlet

# Prints the Test Banner
os.system("clear")
print(Figlet(font='slant').renderText("Test"))

# Initial Interface
mode = bullet.Bullet(
        "Find Project by :",
        choices = ["Get File by ID", "Browse Full Catalog", "Exit"],
        bullet = ">",
        margin = 2,
        ).launch()

# Gets Catalog
catalog = list(csv.reader(open("catalog.txt", "rt")))

# Finding the ID
if (mode == "Get File by ID") :
    os.system("clear")
    print(Figlet(font='slant').renderText("Test"))
    ID = input("ID: ")
elif (mode == "Browse Full Catalog") :
    i = 0
    lim = (len(catalog)-1)//10
    isFound = False
    while (isFound == False):
        os.system("clear")
        print(Figlet(font='slant').renderText("Test"))
        if (i < lim):
            ID = bullet.Bullet(
                    "Page Number %s" %(i+1),
                    choices = ["Back"]+["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[(i*10):(i+1)*10]]+["Next"],
                    bullet = ">",
                    margin = 2
                    ).launch()
            if (ID == "Back"):
                i -= 1
            elif (ID == "Next"):
                i += 1
            else :
                ID = ID[:4]
                isFound = True
        elif (i == lim):
            if (i==0):
                choice = ["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[1:]]
            else :
                choice = ["Back"]+["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[i*10:]]
            ID = bullet.Bullet(
                    "Page Number %s" %(i+1),
                    choices = choice,
                    bullet = ">",
                    margin = 2
                    ).launch()
            if (ID == "Back"):
                i -= 1
            else :
                ID = ID[:4]
                isFound = True
        elif (i == 0):
            ID = bullet.Bullet(
                    "Page Number %s" %(i+1),
                    choices = ["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[1:10]]+["Next"],
                    bullet = ">",
                    margin = 2
                    ).launch()
            if (ID == "Next"):
                i += 1
            else:
                ID = ID[:4]
                isFound = True
else:
    quit()

ID = int(ID)
print("Downloading file with ID", ID)
os.system("wget https://raw.githubusercontent.com/GComputeNerd/rgxttr-repo-test-feature/catalog/"+catalog[ID][3]+".txt")
print("Task Ended. Program Completed!")
