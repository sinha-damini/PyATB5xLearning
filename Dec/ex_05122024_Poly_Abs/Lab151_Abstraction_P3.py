from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def set_gear(self):
        pass




class Engine(GearBox):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass




class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def set_gear(self):
        print("Gearbox is ready")

    def hide_engine(self):
        print("Hide Engine.")


    def hide_gear(self):
        pass


    def drive(self):
        self.start()
        self.set_gear()
        self.stop()
        self.hide_gear()
        self.hide_engine()
        # TypeError: Can't instantiate abstract class Car without an implementation
        # for abstract method 'hide_engine'


car_obj = Car()
car_obj.drive()


print("<<<<<<<<<<<<<<<<<< Practicing >>>>>>>>>>>>>>>>>>")

from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def set_gear(self):
        pass


class Engine():
    @abstractmethod
    def start(self):
        print("Engine Starts")

    @abstractmethod
    def stop(self):
        print("Engine Stops")

class Car(Engine):

    def drive(self):
        self.start()
        # self.set_gear()
        self.stop()


car_obj = Car()
car_obj.drive()
