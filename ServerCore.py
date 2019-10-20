from thespian.actors import *

from time import sleep
from RegionActor import RegionActor

class ServerCore:
    def log(self, message):
        f = open("ServerCore" + ".txt", 'at+')
        f.write("ServerCore: " + str(message) + "\n")
        f.close()

    def tick(self):
        tickOrTock = True

        while True:
            if(tickOrTock):
                print("Tick...")
            else:
                print("...Tock.")

            self.actorSystem.tell(self.regionActor, "tick")

            tickOrTock = not tickOrTock
            sleep(1)


    def __init__(self):
        # this spawns the ActorSystem. All actor types instantiated
        # will be in their own process, and communication between them
        # happens over TCP. 

        # Todo consideration: Consider using the slightly lighter way UDP if it
        # can be guaranteed they are on the same machine. The reason for this is
        # we get the benefit of the lighter weight process and there is no 
        # likelihood of a packet dropping (i.e. the back and forth of TCP is 
        # unnecessary cruft)

        # 'multiprocTCPBase'
        self.actorSystem = ActorSystem('multiprocUDPBase')

        # create an actor, then tell it to spawn 3 guys.
        self.regionActor = self.actorSystem.createActor(RegionActor)
        self.actorSystem.tell(self.regionActor, "spawn")
        self.actorSystem.tell(self.regionActor, "spawn")
        self.actorSystem.tell(self.regionActor, "spawn")

        print ("Main Server Initialized")

