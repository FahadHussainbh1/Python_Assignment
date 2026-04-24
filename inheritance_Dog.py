import inheritance_Animal
class Dog(inheritance_Animal.inheritance_Animal):

    def Fetch(self):
        print(self.name,"Is Fetching")
  




dog= Dog("Burno")
dog.Eat()
dog.Speake()
dog.Fetch()