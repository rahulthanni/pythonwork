# class Staff(object):
#     id:int
#     name:str
#     role:str
#
#     def __init__(self,*args,**kwargs):
#         self.id=kwargs.get("id")
#         self.name=kwargs.get("name")
#         self.role=kwargs.get("role")
#
#     def __str__(self):
#         return self.name
#
#
# user=Staff(id=100,name="rahul",role="admin")
# print(user)



#EMPLOYEE
class Employee:
    def __init__(self,**kwargs):
        self.id=kwargs.get("Id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name



class Department():
    def __init__(self,**kwargs):
        user=kwargs.get("user")
        if user.role=="admin":
            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("no access")

    def __str__(self):
        return self.dept_name


employee=Employee(Id="10212",name="Rahul",role="admin")
dept=Department(dept_name="Development",user=employee)
print(dept)



