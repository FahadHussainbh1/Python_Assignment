class Student:
    __name = "ali"
    __age = 0


    def get_name(self):
        print("Getter Method")
        return self.__name
    
    def Set_name(self,name):
        print("Setter Method")
        self.__name = name

    def get_age(self):
        print("Getter Method for age")
        return self.__age
    
    def Set_age(self,age):
        print("Setter Method for age")
        self.__age = age


student = Student()
print(student.get_name())
print(student.Set_name("fahad"))
print(student.get_name())

print()

print(student.Set_age(20))
print(student.get_age())