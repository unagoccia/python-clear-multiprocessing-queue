# -*- coding: utf-8 -*-

from multiprocessing import Process, Event
from multiprocessing.managers import SyncManager
from PriorityQueue import PriorityQueue, PriorityQueueItem
import random

from TaskWorker import TaskWorker
import Utility

class MyManager(SyncManager): pass
MyManager.register("PriorityQueue", PriorityQueue)
def Manager():
    m = MyManager()
    m.start()
    return m

class RequestHandlingWorker(Process):

    def __init__(self, req_q):
        super(RequestHandlingWorker, self).__init__()
        self.running = Event()
        self.running.clear()
        m = Manager()
        self.tasks_q = m.PriorityQueue()
        self.req_q = req_q

    def run(self):
        num_of_task_worker = 3
        task_workers = [TaskWorker(self.tasks_q, self.running, i) for i in range(num_of_task_worker)]
        for task_worker in task_workers:
            task_worker.start()

        # リクエストを待ち受ける
        while True:
            req = self.req_q.get()
            print 'onRequest: %s' % (req.get_req_json())

            self.clear_tasks()
            self.create_tasks(req)

    def create_tasks(self, req):
        # task_workersを再開
        self.running.set()

        # taskを生成
        print 'created tasks'
        req_date = req.get_date()
        req_data = req.get_data()
        tasks_lst = [PriorityQueueItem(bool(random.getrandbits(1)), {data: req_date}) for data in req_data]

        print '------tasks_lst------'
        for task in tasks_lst:
            print 'priority: %s, contents: %s' % (task.is_priority, task.contents)
        print '---------------------'

        # taskをtaskキューにプッシュ
        for task in tasks_lst:
            self.tasks_q.put(task)

    def clear_tasks(self):
        # task_workersを一時停止
        self.running.clear()

        # taskキューをクリア
        while not self.tasks_q.empty():
            self.tasks_q.get()
        print 'cleared self.tasks_q'
