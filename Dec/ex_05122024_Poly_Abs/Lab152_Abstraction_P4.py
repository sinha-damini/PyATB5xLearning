from abc import ABC, abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        print("Stop the Browser")

    def close_Excel(self):
        print("Close the Browser having Excel.")


class TC1():
    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def close_Excel(self):
        print("Close the Excel.")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()
        self.close_Excel()



tc1 = TC1()
tc1.runTc()
# browse = Browser()
# browse.close_Excel()
# browse.stopBrowser()
#Can't instantiate abstract class Browser
# without an implementation for abstract methods 'readFromExcel', 'startBrowser', 'stopBrowser'