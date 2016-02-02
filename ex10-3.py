# -*- coding: cp1252 -*-
class Player:
    teamcolor = "Blue"
    points = 0

    def __init__(self):
        self.teamcolor=input("What color do I get?: ")
    def tellscore(self):
        print("I am " + self.teamcolor + ", we have" + str(self.points) + " points!")
    def goal(self):
        self.points += 1
    def printout(self):
        print("The" + self.teamcolor + " contender has " + str(self.points) + " points!")

def main():
    player1 = Player()
    player2 = Player()
    player1.goal()
    player1.goal()
    player2.goal()
    player1.tellscore()
    player2.tellscore()

if __name__=="__main__":
    main()