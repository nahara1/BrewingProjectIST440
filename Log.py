import sys
import time
class Log:
    def __init__(self, lid, bs, l, lt, pof):
        self.log_id = lid
        self.brewstage = bs
        self.log = l
        self.log_time = lt
        self._passOrFail = pof

    def generate_log(self):
        return "LogID: {}\n" \
            "Brew Stage: {}\n" \
            "Log: {}\n" \
            "Log Time: {}\n" \
            "Pass or Fail: {}\n".format(self.log_id, self.brewstage, self.log, self.log_time, self._passOrFail)