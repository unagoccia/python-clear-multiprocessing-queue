# -*- coding: utf-8 -*-

from multiprocessing import Process

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

            task = self.tasks_q.get()
            print 'proc(%s) >> task: priority=%s, contents=%s' % (self.proc_num, task.is_priority, task.contents)
            Utility.random_sleep()
