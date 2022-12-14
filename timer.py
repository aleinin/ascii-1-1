from time import perf_counter_ns


class Timer:
    measurement_types = []
    _frames = []
    _frame = []

    def __init__(self, measurement_types):
        self.measurement_types = measurement_types

    def time(self):
        self._frame.append(perf_counter_ns())
        if len(self._frame) == len(self.measurement_types):
            self._frames.append(self._frame)
            self._frame = []

    def get_time(self):
        deltas = []
        for frame in self._frames:
            delta = []
            for i, measurement in enumerate(frame):
                if i == 0:
                    delta.append(0)
                else:
                    delta.append(measurement - frame[i-1])
            deltas.append(delta)
        print_times = {}
        for i in range(1, len(deltas[0])):
            times_list = list(map(lambda j: j[i], deltas))
            times_avg = sum(times_list) / len(times_list)
            times_avg = round(times_avg / 1000000, 4)
            print_times[self.measurement_types[i]] = "{}{}".format(times_avg, "ms")
        print()