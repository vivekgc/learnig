class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    
    def show(self):
        print("Hellow my name is : ",self.name," Working for ", self.company)
obj = Employee("Vivek","Google")
obj.show()

class Former:
    def __init__(self, name , vilage):
        self.name= name
        self.vilage = vilage

    def show(this):
        print("Former ", this.name," from ", this.vilage)

obj = Former("Shourya","Chiradoni")
obj.show()

class student:
    def __init__(self,name,course):
        self.name=name
        self.course = course
    def show(self):
        print("Student ",self.name," From Course" ,self.course)

object = student("Aarya","MBBS")
object.show()