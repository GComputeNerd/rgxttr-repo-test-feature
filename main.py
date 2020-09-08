# Importing Modules
import csv
import bullet
import os

def banner() :
    os.system('clear')
    print("  ______          __")
    print(" /_  __/__  _____/ /_")
    print("  / / / _ \/ ___/ __/")
    print(" / / /  __(__  ) /_")
    print("/_/  \___/____/\__/ \n\n")

# Prints the Test Banner
os.system("clear")
banner()
# Initial Interface
mode = bullet.Bullet(
        "Find Project by :",
        choices = ["Get File by ID", "Browse Full Catalog", "Exit"],
        bullet = ">",
        margin = 2,
        ).launch()

# Gets Catalog
catalog = list(csv.reader(open("catalog.txt", "rt")))
isFound = False

# Finding the ID
if (mode == "Get File by ID") :
    while (isFound == False):
        os.system("clear")
        banner()
        print("Enter 0 to exit")
        ID = int(input("ID: "))
        if (ID > 0 and ID <= len(catalog)):
            isFound = True
        elif (ID == 0):
            quit()
        else:
            input("Invalid ID, press ENTER to Continue...")
elif (mode == "Browse Full Catalog") :
    i = 0
    lim = (len(catalog)-1)//10
    while (isFound == False):
        os.system("clear")
        banner()
        if (i < lim):
            ID = bullet.Bullet(
                    "Page Number %s/%s" %(i+1,lim+1),
                    choices = ["Back"]+["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[(i*10):(i+1)*10]]+["Next","Exit"],
                    bullet = ">",
                    margin = 2
                    ).launch()
            if (ID == "Back"):
                i -= 1
            elif (ID == "Next"):
                i += 1
            elif (ID == "Exit"):
                quit()
            else :
                ID = int(ID[:4])
                isFound = True
        elif (i == lim):
            if (i==0):
                choice = ["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[1:]]+["Exit"]
            else :
                choice = ["Back"]+["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[i*10:]]+["Exit"]
            ID = bullet.Bullet(
                    "Page Number %s/%s" %(i+1,lim+1),
                    choices = choice,
                    bullet = ">",
                    margin = 2
                    ).launch()
            if (ID == "Back"):
                i -= 1
            elif (ID == "Exit"):
                quit()
            else :
                ID = int(ID[:4])
                isFound = True
        elif (i == 0):
            ID = bullet.Bullet(
                    "Page Number %s/%s" %(i+1,lim+1),
                    choices = ["%s - %s by %s" %(x[0],x[3],x[2]) for x in catalog[1:10]]+["Next","Exit"],
                    bullet = ">",
                    margin = 2
                    ).launch()
            if (ID == "Next"):
                i += 1
            elif (ID == "Exit"):
                quit()
            else:
                ID = int(ID[:4])
                isFound = True
else:
    quit()

print("Downloading file with ID", ID)
os.system("wget https://raw.githubusercontent.com/GComputeNerd/rgxttr-repo-test-feature/catalog/"+catalog[ID][3]+".txt")
print("Task Ended. Program Completed!")
