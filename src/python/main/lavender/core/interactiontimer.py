__author__ = 'lewis'

import time


class InteractionTimer:

    @classmethod
    def start(cls):
        return InteractionTimer(time.time())

    def __init__(self, now):
        self._start_time = now
        self._end_time = None

    def stop(self):
        self._end_time = time.time()

    @property
    def is_finished(self):
        return self._end_time is not None

    @property
    def duration(self):
        duration_end = self._end_time if self.is_finished else time.time()
        duration = duration_end - self._start_time
        return duration