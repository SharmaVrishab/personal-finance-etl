def execute(workers):
    # we are mapping here on the files
    for worker in workers:
        worker.map()
    #  store the first -> ie first file like its 100  and use this to add to next files
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)

    return first.result


def map_reduce(worker_cls, input_data_cls, config):
    # orchestrate the workflow here

    #  generate inputs
    inputs = input_data_cls.generate_inputs(config)

    # create worker for each input

    workers = [worker_cls(i) for i in inputs]

    return execute(workers)
