class Distance:
    def __init__(self, start: list[int], end: list[int]):
        self._start = start
        self._end = end

    def distance(self):
        first_addition = (self._end[0] - self._start[0]) ** 2
        second_addition = (self._end[1] - self._start[1]) ** 2
        result = first_addition + second_addition

        return abs(result ** 0.5)
