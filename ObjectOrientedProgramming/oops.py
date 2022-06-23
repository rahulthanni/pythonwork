class Student:
    def __init__(self,name,rollno,gender):
        self.name=name
        self.rollno=rollno
        self.gender=gender
    def print_student(self):
        print(self.name,self.rollno,self.gender)

s1=Student("Rahul",10,"male")

s1.print_student()
