class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        # * process the data and store them in result
        raise NotImplementedError

    def reduce(self):
        # * combine data of other worker here
        raise NotImplementedError
