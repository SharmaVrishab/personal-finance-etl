import os
import random

# from mapreduce.framework import map_reduce
# from mapreduce.input_data import PathInputData
# from mapreduce.worker import LineCountWorker
from mapreduce import LineCountWorker, PathInputData, map_reduce


def write_test_files(tmpdir):
    os.makedirs(tmpdir, exist_ok=True)
    for i in range(10):
        with open(os.path.join(tmpdir, str(i)), "w") as f:
            f.write("\n" * random.randint(0, 100))


if __name__ == "__main__":
    tmpdir = "test_inputs"
    write_test_files(tmpdir)

    config = {"data_dir": tmpdir}
    result = map_reduce(LineCountWorker, PathInputData, config)
    print(f"There are {result} lines")
