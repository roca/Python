def occurrences(a):
    counts = [0] * len(a)
    for i,e1 in enumerate(a):
        b = a[:i] + a[i+1:]
        for e2 in b:
            if e1 == e2:
               counts[i] += 1
    return counts

def leader(a):
    counts = occurrences(a)
    for i,e in enumerate(counts):
        if (2*e) > len(a):
            return a[i]
    return -1

def sum(total,a):
    if len(a) == 0:
        return total
    else:
        total += a[0]
        return sum(total, a[1:])

def equilibrium(a):
    for i,e in enumerate(a):
        left = sum(0,a[:i])
        right = sum(0,a[i+1:])
        if (left == right and i != 1):
            return f'index: {i} ,element: {e}'
    return -1

