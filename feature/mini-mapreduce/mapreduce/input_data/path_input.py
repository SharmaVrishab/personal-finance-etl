import os

from .base_input_data import InputData


#  we reading files here
class PathInputData(InputData):
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]
        #  looping though each file in the directory
        for filename in os.listdir(data_dir):
            # create an instance of the class (or subclass) with the file path as its argument.
            # here with yield we created generator
            yield cls(os.path.join(data_dir, filename))
