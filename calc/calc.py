class MinMax:
    """ Provides minimum and maximum of added values. """

    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    @property
    def min(self):
        if self.values:
            return min(self.values)
        return None

    @property
    def max(self):
        if self.values:
            return max(self.values)
        return None


def find_zeros(l, minmax, depth=1):
    """ Recursively search for occurrences of 0 and store depth. """

    for i in l:
        if isinstance(i, list):
            find_zeros(i, minmax, depth + 1)
        if i == 0:
            minmax.add(depth)

    return minmax


def calculate_depth(l):
    if not isinstance(l, list):
        return [None, None]

    found = find_zeros(l, MinMax())
    return [found.min, found.max]
