class Model:

    def __init__(self)->None:
        pass

    def interpret(self, model, output):
        for function in model.functions:
            function.interpret(output)
            
                
                