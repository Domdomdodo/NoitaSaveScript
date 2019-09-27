import os
import shutil

appdataLoc = os.getenv('APPDATA')
cwd = os.getcwd()
if not os.path.exists(cwd + "\\saves"):
    os.makedirs(cwd + "\\saves")

appdataLoc = appdataLoc.replace("\\Roaming","")
saveLoc = appdataLoc + '\\LocalLow\\Nolla_Games_Noita\\save00'

filesToMove = ("world_state.salakieli","player.salakieli","magic_numbers.salakieli","world")

def showCommands():
    print("Use /save (name) to create a new savegame with the current game state")
    print("Use /load (name) to load a previously saved savegame")
    print("Use /delete (name) to delete a previously saved savegame")
    print("Use /list to show previously saved savegames")
    print("Use /help to display this list.")
    print("Use /sugma :)")

def loadSave(argument):
    if not os.path.exists(cwd + "\\saves\\" + argument):
        print("This savegame does not exist!")
    else:
        try:
            for file in filesToMove:
                if not file == "world":
                    if  os.path.exists(saveLoc + "\\" + file):
                        os.remove(saveLoc + "\\" + file)
                    shutil.copy(cwd + "\\saves\\" + argument + "\\"  + file , saveLoc + "\\")
                else:
                    if  os.path.exists(saveLoc + "\\" + file):
                        shutil.rmtree(saveLoc + "\\" + file)
                    shutil.copytree(cwd + "\\saves\\" + argument + "\\" + file, saveLoc + "\\" + "world")
            print("Game loaded!")
        except:
            try:
                os.removedirs(cwd + "\\saves\\" + argument)
                print("Loading file failed, please try again.")
            except:
                print("Loading file failed, please try again.")
                print("Cleanup failed, if your game acts up you might want to manually clean the save location.")

def deleteSave(argument):
    if not os.path.exists(cwd + "\\saves\\" + argument):
        print("This savegame does not exist!")
    else:
        try:
            shutil.rmtree(cwd + "\\saves\\" + argument)
            print("Save deleted!")
        except:
            print("Deleting failed, try running this script as an admin.")

def list():
    i = 0
    for (dirpath, dirnames, filenames) in os.walk(cwd + "\\saves\\"):
        if len(dirnames) == 0:
            print("No saves found, try using /save (name).")
            break
        for name in dirnames:
            if not name == "world":
                i += 1
                print(str(i) + " - " + name)
        break

def saveGame(argument):
    if os.path.exists(cwd + "\\saves\\" + argument):
        print("This savegame already exists!")
    else:
        os.makedirs(cwd + "\\saves\\" + argument)
        try:
            for file in filesToMove:
                if not file == "world":
                    shutil.copy(saveLoc + "\\" + file, cwd + "\\saves\\" + argument + "\\")
                else:
                    shutil.copytree(saveLoc + "\\" + file, cwd + "\\saves\\" + argument + "\\" + "world")
            print("Game saved!")
        except:
            try:
                os.removedirs(cwd + "\\saves\\" + argument)
                print("One or more of the save files couldn't be found, the save was cancelled.")
            except:
                print("One or more of the save files couldn't be found, the save was cancelled.")
                print("Cancelling the save failed too, because apparently this script is worthless or it's not allowed to remove the mess it leaves behind.")
                print("You might want to /delete the save you tried to create or manually remove the broken save, loading it might be a bad idea")


keepGoing = True
print("Welcome to this Noita savegame script")
print("WARNING: Use this script at your own risk! Back-up your current save AND stats!")
print("Use /help to show available commands")
while keepGoing:
    command = input()
    commandCheck = command
    validCommand = False

    if command.startswith("/help"):
        showCommands()
        validCommand = True

    if command.startswith("/sugma"):
        print("dick")
        validCommand = True
        
    if command.startswith("/list"):
        list()
        validCommand = True
        
    if command.startswith("/save"):
        command = command.replace("/save ","")
        saveGame(command)
        validCommand = True
        
    if command.startswith("/load"):
        command = command.replace("/load ","")
        loadSave(command)
        validCommand = True
        
    if command.startswith("/delete"):
        command = command.replace("/delete ","")
        deleteSave(command)
        validCommand = True
        
    if not validCommand:
        print("This command is invalid, try again!")
