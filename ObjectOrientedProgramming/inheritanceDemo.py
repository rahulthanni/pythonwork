class Parent:
    def phone(self):
        print("Nokia 6.1 plus")
    def bike(self):
        print("passion pro")

class Child(Parent):
    # pass
    def phone(self):
        print("Iphone 12")
    def bike(self):
        print("Duke")

ch=Child()
ch.phone()
ch.bike()