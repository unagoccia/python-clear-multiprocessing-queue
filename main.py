# -*- coding: utf-8 -*-

from multiprocessing import Queue
import random
import json

from RequestHandlingWorker import RequestHandlingWorker
from Request import Request
import Utility

def main():
    req_q = Queue()
    req_handle_worker = RequestHandlingWorker(req_q)
    req_handle_worker.start()

    while True:
        Utility.random_sleep()

        dummy_request_str = Utility.random_str(random.randint(10, 60))
        req_json = {
            'date': '20171210',
            'dummy_data': [Utility.random_str(5) for i in range(10)]
        }

        request = Request()
        request.set_req_json(json.dumps(req_json))
        print 'main >> request.set_req_json: %s' % (request.get_req_json())
        req_q.put(request)

if __name__ == "__main__":
    main()
