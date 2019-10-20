from thespian.actors import *
import os

# An Actor...
class GuyActor(Actor):
    # self.myAddress
    hunger = 0
    sleep = 0

    def log(self, message):
        f = open("GuyActor" + ".txt", 'at+')
        f.write("Guy(" + str(self.myAddress) + "): " + str(message) + "\n")
        f.close()

    def tick(self):
        self.hunger = self.hunger + 1
        self.sleep = self.sleep + 1
        self.log("tick: " + str(self.hunger) + "\t" + str(self.sleep))

    def receiveMessage(self, message, sender):
        if(message == "tick"):
            self.tick()


