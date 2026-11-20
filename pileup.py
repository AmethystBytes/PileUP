import json
import os
import time
import random
from pathlib import Path

def pileupSafetyTeam():
    print("PileUP SafetyTeam")
    print("-----------------")
    confirmClean(noBranding=0)
    scPackID = "1"
    scSearchResult = None
    scRemovalTest = None
    packages.append({"PackID": "1", "Sender": "Me", "Sender DOL": "Here", "Recipient": "Him", "Recipient PUL": "There", "Size": "Default", "Status": "Testing"})
    saveJSON()
    print ("\033[1;30;43m Package Creation/Reading Test \033[0;0m")
    for package in packages:
        if package["PackID"] == scPackID:
            scSearchResult = package
            break
    if(scSearchResult == None):
        print("Package Creation/Reading failed!")
        quit(2)
    else:
        print("Package Creation/Reading finished successfully!")
        print ("\033[1;30;43m Package Status Change Test \033[0;0m")
        scSearchResult["Status"] = "PSCT"
        saveJSON()
        if(scSearchResult["Status"] == "PSCT"):
            print("Package Status Change finished successfully!")
            print ("\033[1;30;43m Package Removal Test \033[0;0m")
            packages.remove(scSearchResult)
            saveJSON()
            for package in packages:
                if package["PackID"] == scPackID:
                    scRemovalTest = package
                    break
            if(scRemovalTest == None):
                print("Package Removal finished successfully!")
                time.sleep(1)
                startMenu()
            else:
                print("Package Removal failed!")
                quit(4)
        else:
            print("Package Status Change failed!")
            quit(3)

pathJSON = "packages.json"

path = Path(pathJSON)
packages = json.loads(path.read_text()) if path.exists() else []

def startMenu():
    confirmClean(noBranding=1)
    os.system("cls" if os.name == "nt" else "clear")
    print("PileUP Package Management Service")
    print("---------------------------------")
    print("1. Enter a new package")
    print("2. Manage a package")
    print("3. List packages")
    print("4. PileUP settings")
    print("Please choose your menu option: ")
    menuInput = input()
    if(menuInput == "1"):
        os.system("cls" if os.name == "nt" else "clear")
        print("PileUP Package Management Service")
        print("---------------------------------")
        PackIDCode = random.randrange(10000000,99999999)
        print("Please enter the sender")
        sender = input()
        print("Please enter the sender DOL")
        senderDOL = input()
        print("Please enter the recipient")
        recipient = input()
        print("Please enter the recipient PUL")
        recipientPUL = input()
        print("Please enter the package size")
        size = input()
        packages.append({"PackID": PackIDCode, "Sender": sender, "Sender DOL": senderDOL, "Recipient": recipient, "Recipient PUL": recipientPUL, "Size": size, "Status": "Starting Location"})
        saveJSON()
        os.system("cls" if os.name == "nt" else "clear")
        startMenu()
    elif(menuInput == "2"):
        os.system("cls" if os.name == "nt" else "clear")
        packageManage()
    elif(menuInput == "3"):
        os.system("cls" if os.name == "nt" else "clear")
        print("PileUP Package Management Service")
        print("---------------------------------")
        print("Packages:")
        print("")
        for package in packages:
            print("----------------------------------------------------")
            print("PackID: ", package["PackID"]," ","Status: ", package["Status"])
            print("Sender:", package["Sender"], " ","Recipient: ", package["Recipient"])
            print("Sender Drop Off Location: ", package["Sender DOL"])
            print("Recipient Pick Up Location: ", package["Recipient PUL"])
            print("----------------------------------------------------")
            print("")
        print("")
        print("Type leave to exit")
        listInput = input()
        if(listInput == "leave"):
            exitCommand()
    elif(menuInput == "4"):
        settings()
    elif(menuInput == "leave"):
        exitCommand()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Please enter a vaild command!")
        time.sleep(3)
        startMenu()

def packageManage():
    print("PileUP Package Management Service")
    print("---------------------------------")
    print("Please enter your PackID below:")
    PackIDInput = int(input())
    packageSearchResult = None
    for package in packages:
        if package["PackID"] == PackIDInput:
            packageSearchResult = package
            break
    if packageSearchResult == None:
        print("No package was found. Please try again")
        time.sleep(3)
        startMenu()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("PileUP Package Management Service")
        print("---------------------------------")
        print("Package found! Choose how to manage: ")
        print("1. Change the status")
        print("2. Remove the package")
        packageManageInput = input()
        if(packageManageInput == "1"):
            os.system("cls" if os.name == "nt" else "clear")
            print("PileUP Package Management Service")
            print("---------------------------------")
            print("Package current status: ",packageSearchResult["Status"])
            print("(If you enter Arrived, it will delete the package)")
            print("Please enter the new status of this package: ")
            statusInput = input()
            if(statusInput == "Arrived"):
                os.system("cls" if os.name == "nt" else "clear")
                removePackage(psr=packageSearchResult)
            else:
                packageSearchResult["Status"] = statusInput
            saveJSON()
            startMenu()
        elif(packageManageInput == "2"):
            removePackage(psr=packageSearchResult)
        else:
            print("Please enter a vaild option!")
            time.sleep(3)
            packageManage()

def saveJSON():
    path.write_text(json.dumps(packages, indent=2))

def reloadPackages():
    global packages
    packages = json.loads(path.read_text()) if path.exists() else []

def removePackage(psr=None):
    print("PileUP Package Management Service")
    print("---------------------------------")
    print("Please confirm that you want to remove (YES or anything):")
    removalConfirm = input()
    if(removalConfirm == "YES"):
        os.system("cls" if os.name == "nt" else "clear")
        print("Deleting")
        packages.remove(psr)
        saveJSON()
        time.sleep(3)
        startMenu()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Cancelling")
        time.sleep(3)
        startMenu()

def settings():
    os.system("cls" if os.name == "nt" else "clear")
    print("PileUP Package Management Service")
    print("---------------------------------")
    print("1. JSON Save Location")
    print("2. Change JSON file location")
    print("3. Preform PileUP SafetyTeam")
    print("4. Preform ConfirmClean")
    print("Please choose your menu option: ")
    debugInput = input()
    if(debugInput == "1"):
        print("--------")
        print(path.resolve())
        print("--------")
        time.sleep(5)
        settings()
    elif(debugInput == "2"):
        os.system("cls" if os.name == "nt" else "clear")
        print("Choose your JSON file location: ")
        pathJSON = input()
        settings()
    elif(debugInput == "3"):
        pileupSafetyTeam()
    elif(debugInput == "4"):
        confirmClean()
        settings()
    elif(debugInput == "leave"):
        exitCommand()
    else:
        print("Please enter a valid command!")
    

def confirmClean(noBranding=0):
    PackIDcc = 1
    if(noBranding==0):
        print("\033[1;30;46m ConfirmClean \033[0;0m")
        print("PileUP SafetyTeam Cleanup")
        for package in packages:
            if "PackID" in package and package["PackID"] == PackIDcc:
                packages.remove(package)
                break
        time.sleep(1)
    else:
        for package in packages:
            if "PackID" in package and package["PackID"] == PackIDcc:
                packages.remove(package)
                break

def exitCommand():
    os.system("cls" if os.name == "nt" else "clear")
    print("Would you like to kill the program or go to the menu?")
    print("1. Main Menu")
    print("2. Kill")
    exitInput = input()
    if(exitInput == "1"):
        os.system("cls" if os.name == "nt" else "clear")
        startMenu()
    elif(exitInput == "2"):
        os.system("cls" if os.name == "nt" else "clear")
        quit(1)

pileupSafetyTeam()