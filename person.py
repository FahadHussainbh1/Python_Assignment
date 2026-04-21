class Person : 
    name = "Fahad"
    age = 18

    def __init__(self):
        print("Introduction")

    def introduce(self,name,age):
        self.name = name
        self.age = age
        print("My name is:",self.name,"my age is:",self.age)




person_1 = Person()
print(person_1.name)
print(person_1.age)

person_1.introduce("Hussain",18)
person_1.introduce("Fahad",20)
print(person_1.name)
print(person_1.age)

person_1.introduce("Mudasir",23)
print(person_1.name)
print(person_1.age)

