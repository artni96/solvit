def my_range(end: int, start: int | None = None, step: int = 1):
    if step == 0:
        raise ValueError
    if step > 0:
        if start:
            start, end = end, start
        else:
            start = 0
        counter = start
        yield counter

        while end - step > counter:
            counter += step
            yield counter

    elif step < 0:
        start, end = end, start
        counter = start
        yield counter
        while end - step< counter:
            counter += step
            yield counter



test_result = my_range(10, 2, -1)
for elem in test_result:
    print(elem)
