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

# Vehicle and its subclasses BEGIN
class Vehicle:
    '''Parent Class to GroundVehicle and Grandaprent Class to Car Class'''
    pass

class GroundVehicle(Vehicle):
    '''GV extends Vehicle, its only parent. Takes all attrs of Vehicle'''
    pass

class Car(GroundVehicle):
    '''Car extends GV and takes all of GV + Vehicle attrs'''
    pass

class Motorcycle(GroundVehicle):
    '''Motorcycle extends GV and takes all of GV + Vehicle attrs'''
    pass
# Vehicle and its subclasses END
################################

# FlightVehicle and its subclass BEGIN
class FlightVehicle(Vehicle):
    '''Parent Class to Airplane class only.'''
    pass

class Airplane(FlightVehicle):
    '''Airplane Class extends Airplane class and takes all airplane attrs.'''
    pass

# FlightVehicle and its subclass END
################################

# Starship is a stand alone class. NO subclasses 
class Starship(FlightVehicle):
    '''Parent Class to nothing.'''
    pass


