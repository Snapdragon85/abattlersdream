import time
import sys

import command

print("A BATTLER'S DREAM")
start = input("Begin game? (y/n)")
if start == "y":
    print("Begin Fight!")
    command.clear()
    command.battle()

if start == "n":
    print("Goodnight!")
    time.sleep(1)
    sys.exit()