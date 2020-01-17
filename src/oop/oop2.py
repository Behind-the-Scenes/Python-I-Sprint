# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        return 'vroooom'

lambo = GroundVehicle()
print(f'\n The Lambo with {lambo.num_wheels} wheels goes {lambo.drive()} {lambo.drive()}! \n')


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO
class Motorcycle(GroundVehicle):

    def __init__(self, num_wheels = 4):
        super().__init__(num_wheels=2)
    def drive(self):
        return 'BRAAAP!!'
    

m1 = Motorcycle()
print(f' A Motorcycle with {m1.num_wheels} wheels goes {m1.drive()} {m1.drive()}. \n')


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go (loop) through the vehicles list and print the result of calling drive() on each.

# TODO

for x in vehicles:
    print(f' I am driving loop {x.drive()}')
