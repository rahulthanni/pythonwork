class Course:
    course_name:str
    status:bool
    def add_Course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")

    def __str__(self):
        return self.course_name

class Batch:

    course:Course
    batch_code:str
    strt_dt:str

    def add_batch(self,**kwargs):
            self.course=kwargs.get("Course")
            self.batch_code=kwargs.get("Batch_code")
            self.strt_dt=kwargs.get("Start_date")
    def __str__(self):
        return self.batch_code

class Student:
    student_name:str
    gender:str
    batch:Batch

    def add_Student(self,**kwargs):
            self.student_name=kwargs.get("Student_Name")
            self.gender = kwargs.get("Gender")
            self.batch=kwargs.get("Batch")


    def __str__(self):
        return self.student_name


django=Course()
django.add_Course(course_name="Django",status="True")
bigdata=Course()
bigdata.add_Course(course_name="BigData",status="True")
db1=Batch()
db1.add_batch(Batch_Code="djMay2022",Course=django,strt_dt="18-05-2022")
bd1=Batch()
bd1.add_batch(Batch_Code="bgMay2022",Course=bigdata,strt_dt="20-05-2022")

rahul=Student()
rahul.add_Student(Student_Name="Rahul",Gender="Male",Batch=db1)

pranav=Student()
pranav.add_Student(Student_Name="Pranav",Gender="Male",Batch=db1)

lakshmi=Student()
lakshmi.add_Student(Student_Name="Lakshmi",Gender="Female",Batch=bd1)

print(lakshmi.batch.course.course_name)




