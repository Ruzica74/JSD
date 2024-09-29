class SimpleOrComplexValue:
    def interpret(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class SimpleValue(SimpleOrComplexValue):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        


class ComplexValue(SimpleOrComplexValue):
    def __init__(self, parent, pointer=None, elements=None):
        self.parent = parent
        self.pointer = pointer
        self.elements = elements or []

    def interpretSpecification(self, name, type, counter):
        output = "    "+str(counter)+". Define the "+ name +"_example of "+type+" type with the following elements:\n"
        for member in self.elements:
            output += "  • " + member.memberName +" = "+ str(member.memberValue)+"\n"
        return output

class PointerValue(SimpleOrComplexValue):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def interpretSpecification(self, name, type, counter):
        output = "    "+str(counter)+". Define the "+ name +"_example of "+type+" type with the following value "+str(self.value)+".\n"
        return output

