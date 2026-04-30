import Animal as a 
import Dog as d
import Horse as h

animal = a.Animal()
dog = d.Dog()
horse = h.Horse()

list = [animal,dog,horse]

for x in list:
    x.eat()