def predicate(x):
    if x <= 3:
        return True
    return False


def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x


d = dropwhile(predicate, [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0])
list(d)
