

def combinations3(iterable, r):
    # ABCDEFG
    # 3
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return None

    indices = list(range(r))  # start out as [0, 1, 2]

    yield tuple(pool[i] for i in indices)
    # ("A", "B", "C") 0, 1, 2
    # ("A", "B", "D") 0, 1, 3 ...
    while True:

        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return None

        indices[i] += 1

        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1

        yield tuple(pool[i] for i in indices)


def combinations2(iterable, r):
    """
    1.  create a tuple from the iterator
    2.  determine if r is too big for the iterable size
    3.  get the indices corresponding to r
    4.  yield the first tuple (will always be the first r elements of the iterable in sequential order; A, B, C, above)
    5.  loop through the remaining n choose r - 1 combinations
    6.  add 1 to the current index if certain conditions are met
    7.  and yield the tuple ( ABx, x = C, D, E, F, G )

    """
    # 1.
    pool = tuple(iterable)
    # 2.
    n = len(pool)
    if r > n:
        return
    # 3.
    indices = list(range(r))
    # 4.

    yield tuple(pool[i] for i in indices)

    # 5.
    while True:
        # 6.
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        # 7.
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

        yield tuple(pool[i] for i in indices)


print(list(combinations2("ABCDEFG", 3)) == list(combinations3("ABCDEFG", 3)))

