import Vahicle as v
import Car as c
import Plane as p

vahicle = v.Vahicle()
car = c.Car()
plane = p.Plane()

list = [vahicle,car,plane]

for y in list:
    y.move()