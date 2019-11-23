# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#base class
#  [Vehicle]
class Vehicle:
    def __init__(self):
      pass

#  [Vehicle]
#      |                
#      v                
# [GroundVehicle] 
class GroundVehicle(Vehicle):
    def __init__(self):
      super().__init__()
      pass


#  [Vehicle]
#      |                
#      v                
# [GroundVehicle]      
#   |       
#   v       
# [Car]  
class Car(GroundVehicle):
    def __init__(self):
      super().__init__()
      pass


#  [Vehicle]
#      |                
#      v                
# [GroundVehicle]      
#           |
#           v
#      [Motorcycle]
class Motorcycle(GroundVehicle):
    def __init__(self):
      super().__init__()
      pass

#[Vehicle]->[FlightVehicle]
class FlightVehicle(Vehicle):
    def __init__(self):
      super().__init__()
      pass

#[Vehicle]->[FlightVehicle]
#                       |
#                       v
#                  [Airplane]
class Airplane(FlightVehicle):
    def __init__(self):
      super().__init__()
      pass

#[Vehicle]->[FlightVehicle]->[Starship]
class Starship(FlightVehicle):
    def __init__(self):
      super().__init__()
      pass

