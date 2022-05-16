def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable) # tuple('abc') => ('a','b','c')
    n = len(pool)
    if not n and r: # 0 and 0 => True
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    
    while True:
        for i in reversed(range(r)): # r-1,r-2,...,0
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)