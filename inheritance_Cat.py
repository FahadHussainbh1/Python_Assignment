import inheritance_Animal
class Cat(inheritance_Animal.inheritance_Animal):


    def Walk(self):
        print(self.name,"is Walking")




cat = Cat("Kitty")
cat.Eat()
cat.Speake()
cat.Walk()

