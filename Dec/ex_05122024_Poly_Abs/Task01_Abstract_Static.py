# Create a Program
#
# Parent Class - PC
#
# Class - MotherBoard
# Method → start MotherBoard
#
# abs Class - RAM
# abstractMethod → start ram
#
# abs Class - Processor
# abstractMethod → start processor
#
# abs Class - Storage
# abstractMethod → storage data,

# In PC:
# static method -> loadOS
#
# non static -> startMouse, UseHeadPhone

from abc import ABC, abstractmethod

class PC():
    def __init__(self):
        print("Started the PC.")

    @staticmethod
    def loados():
        print("OS Loaded.")

    def startmouse(self):
        print("Start using the mouse")

    def useheadphone(self):
        print("Plugin the headphone to hear sound")

class motherboard():
    def start(self):
        print("Start the motherboard")

class RAM(ABC):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):
    @abstractmethod
    def start_processor(self):
        pass

class Storage(ABC):
    @abstractmethod
    def data_storage(self):
        pass


o1 = PC()
PC.loados()
o1.startmouse()
o1.useheadphone()