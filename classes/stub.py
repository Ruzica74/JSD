class StubDefinition:
    def __init__(self, parent, stubFuncName, stubValue, stubCallback):
        self.parent = parent
        self.stubFuncName = stubFuncName
        self.stubValue = stubValue
        self.stubCallback = stubCallback