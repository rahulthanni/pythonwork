class P1:
    def m1(self):
        print("Inside m1")
class P2(P1):
    def m2(self):
        print("Inside m2")
class P3(P2):
    def m3(self):
        print("Inside m3")

P3=P3()
P3.m3()
P3.m2()
P3.m1()
