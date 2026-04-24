class Animal:
    name = ""
    sound = ""
    eat = ""

    def __init__(self,name):
        self.name = name

    def Speake(self):
        print(self.name,"is says")

    def Eat(self):
        print(self.name,"is eats")
            


# Child Class    
class Dog(Animal):

    def Fetch(self):
        print(self.name,"Is Fetching")
  
dog= Dog("Burno")
dog.Eat()
dog.Speake()
dog.Fetch()


print()

# Child Class
class Cat(Animal):


    def Walk(self):
        print(self.name,"is Walking")


cat = Cat("Kitty")
cat.Eat()
cat.Speake()
cat.Walk()



    