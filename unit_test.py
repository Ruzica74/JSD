from os.path import dirname, join
from textx import metamodel_from_file, TextXSyntaxError, TextXError
from textx.export import metamodel_export, model_export
import argparse
from classes.case import CaseDefinition
from classes.model import Model
from classes.function import FunctionDefinition
from classes.stub import StubDefinition
from classes.value import ComplexValue, PointerValue, SimpleOrComplexValue, SimpleValue




def main(debug=False):

    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-i', '--input', type=str, help="Input file that contains defined functions", required=True)
    parser.add_argument('-o', '--output', type=str, help="Output file with created unit tests", required=True)

    # Parse the arguments
    args = parser.parse_args()

    this_folder = dirname(__file__)
    try:
        unit_mm = metamodel_from_file(join(this_folder, 'grammar.tx'),classes=[ FunctionDefinition, CaseDefinition, 
        SimpleOrComplexValue, SimpleValue, ComplexValue, PointerValue, StubDefinition], debug=False)
        unit_model = unit_mm.model_from_file(join(this_folder, args.input))
        newModel = Model()
        newModel.interpret(unit_model, args.output)
    #metamodel_export(unit_mm, join(this_folder, 'unit_meta.dot'))
    except TextXError as e:
        print(f"An exception occurred: {e}")
        print(f"Type of exception: {type(e)}")


if __name__ == "__main__":
    main()