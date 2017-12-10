# -*- coding: utf-8 -*-

import json

class Request(object):

    def __init__(self):
        super(Request, self).__init__()
        self.req_json = None

    def set_req_json(self, req_json):
        self.req_json = req_json

    def get_req_json(self):
        return self.req_json

    def get_date(self):
        json_dict = json.loads(self.req_json)
        return json_dict['date']

    def get_data(self):
        json_dict = json.loads(self.req_json)
        return json_dict['dummy_data']
