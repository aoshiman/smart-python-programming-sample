# -*- coding: utf-8 -*-

import time

class Sample(object):

    def do_something(self):
        self._take_a_log_time()
        return 'Hello, World!'

    def _take_a_log_time(self):
        time.sleep(10)
