from thespian.actors import *
from GuyActor import GuyActor

# An Actor...
class RegionActor(Actor):
    regionActors = []

    # self.myAddress
    def tick(self):
        for actor in self.regionActors:
            self.log("tick")
            self.send(actor, "tick")

    def log(self, message):
        f = open("RegionActor" + ".txt", 'at+')
        f.write("Region(" + str(self.myAddress) + "): " + str(message) + "\n")
        f.close()

    def spawn(self):
        newActor = self.createActor(GuyActor)
        
        self.regionActors.append(newActor)
        self.log("Spawned Actor: " + str(newActor))

    def receiveMessage(self, message, sender):
        if(message == "spawn"):
            self.spawn()
        elif(message == "tick"):
            self.tick()
        
        

