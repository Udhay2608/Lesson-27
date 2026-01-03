class Vehicle:
     def __init__(self,name,maxspeed,mileage):
          self .name=name
          self.maxspeed=maxspeed
          self.mileage=mileage

class Bus(Vehicle):
     pass
School_bus=Bus("School Volvo",180,12)
print("Vehicle name ",School_bus.name,"speed",School_bus maxspeed,"Mileage",School_bus.mileage)