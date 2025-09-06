class InputData:
    def read(self):
        # for returning raw data
        raise NotImplementedError

    @classmethod
    def generate_inupts(cls, config):
        # factory method that has multiple return type
        raise NotImplementedError
