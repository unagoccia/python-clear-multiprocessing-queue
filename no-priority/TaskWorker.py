# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue

import Utility

class TaskWorker(Process):

    def __init__(self, tasks_q, running, proc_num):
        super(TaskWorker, self).__init__()
        self.tasks_q = tasks_q
        self.running = running
        self.proc_num = proc_num

    def run(self):
        while True:
            if not self.running.is_set():
                print 'proc(%s) >> pause' % (self.proc_num)

            # 実行待機
            self.running.wait()

            # task = self.tasks_q.get()
            # print 'proc(%s) >> task: %s' % (self.proc_num, task)
            while not self.tasks_q.empty():
                try:
                    task = self.tasks_q.get(True, 10)
                    print 'proc(%s) >> task: %s' % (self.proc_num, task)
                except:
                    print 'warn: catch error'
            Utility.random_sleep()
