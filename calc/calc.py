class MinMax():
    """ Keeps minimum and maximum of added values. """

    def __init__(self, min_value=None, max_value=None):
        self._min = min_value
        self._max = max_value
    
    def add(self, value):
        if self._min == None:
            self._min = value
        else:
            self._min = min(self._min, value)
        
        if self._max == None:
            self._max = value
        else:
            self._max = max(self._max, value)


def find_zeros(l, minmax, depth=1):
    for i in l:
        if isinstance(i, list):
            find_zeros(i, minmax, depth+1)
        if i == 0:
            minmax.add(depth)
    
    return minmax


def calculate_depth(l):
    if not isinstance(l, list):
        return [None, None]
    
    found = find_zeros(l, MinMax())
    return [found._min, found._max]
