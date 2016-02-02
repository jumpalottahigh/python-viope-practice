class Player:
    teamcolor = "Blue"
    points = "300"

    def printout(self):
        print("The " + self.teamcolor + " contender has " + self.points + " points!")

def main():
    player1 = Player()
    player1.teamcolor = "Blue"
    player1.points = "300"
    player1.printout()

if __name__=="__main__":
    main()