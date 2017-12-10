# -*- coding: utf-8 -*-

from heapq import heappush, heappop
import time

class PriorityQueueItem(object):
    def __init__(self, is_priority, contents):
        PRIORITY = 1
        NO_PRIORITY = 10
        self.is_priority = is_priority
        self.priority = PRIORITY if is_priority else NO_PRIORITY
        self.contents = contents
        return

    def __le__(self, other):
        return self.priority <= other.priority

class PriorityQueue(object):
    def __init__(self, maxsize=None):
        self.queue = []
        self.maxsize = maxsize
    def __len__(self):
        return len(self.queue)
    def __contains__(self, item):
        return item in self.queue
    def empty(self):
        return self.__len__() == 0
    def full(self):
        if self.maxsize is not None:
            return self.__len__() == self.maxsize
        return False
    def put(self, value):
        while self.full():
            time.sleep(0.01)
        heappush(self.queue, value)
    def get(self):
        while self.empty():
            time.sleep(0.01)
        return heappop(self.queue)
