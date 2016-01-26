# -*- coding: cp1252 -*-
import string
import random

won = 0
played = 0
tie = 0

while True:

    player = str(input("Foot, Nuke or Cockroach? (Quit ends): "))

    if player == "Quit":
        print("You played " + str(played) + " rounds, and won " + str(won) + " rounds, playing tie in " + str(tie) + " rounds.")
        exit()

    if player != "Foot" and player != "Nuke" and player != "Cockroach":
        print("Incorrect selection.")
        continue

    else:
        cpu = random.randint(0,3)
        if cpu == 1:
            cpu = "Foot"
        elif cpu == 2:
            cpu = "Nuke"
        else:
            cpu = "Cockroach"

        print("You chose: " + player + "\nComputer chose: " + cpu)

        if player == "Nuke" and cpu == "Nuke":
            print("Both LOSE!")
        elif player == cpu:
            print("It is a tie!")
            tie = tie + 1
        elif player == "Nuke" and cpu == "Foot":
            print("You WIN!")
            won = won + 1
        elif player == "Foot" and cpu == "Cockroach":
            print("You WIN!")
            won = won + 1
        elif player == "Cockroach" and cpu == "Nuke":
            print("You WIN!")
            won = won + 1
        else:
            print("You LOSE!")

        played = played + 1