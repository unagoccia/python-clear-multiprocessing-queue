# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue, Event

from TaskWorker import TaskWorker
import Utility

class RequestHandlingWorker(Process):

    def __init__(self, req_q):
        super(RequestHandlingWorker, self).__init__()
        self.running = Event()
        self.running.clear()
        self.tasks_q = Queue()
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
        dummy_tasks = ['%s_%s' % (req_date, data) for data in req_data]
        print dummy_tasks

        # taskをtaskキューにプッシュ
        for task in dummy_tasks:
            self.tasks_q.put(task)

    def clear_tasks(self):
        # task_workersを一時停止
        self.running.clear()

        # taskキューをクリア
        while not self.tasks_q.empty():
            self.tasks_q.get()
        print 'cleared self.tasks_q'
