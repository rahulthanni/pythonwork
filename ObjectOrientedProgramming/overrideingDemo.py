class Parent:

    def properties(self) -> str:
        self.props={"mobile":"nokia", "bike":"passionpro"}
        return self.props

class Child(Parent):
    def properties(self) -> str:
        props=super().properties()
        props["car"]="swift"
        return props

ch=Child()
print(ch.properties())