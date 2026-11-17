import time
import sys

print("A BATTLER'S DREAM")
start = input("Begin game? (y/n)")
if start == "y":
    print("Begin Fight!")
    
if start == "n":
    print("Goodnight!")
    time.sleep(1)
    sys.exit()