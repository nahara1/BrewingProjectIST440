# Team Boil
# Created By Alex Hirsh, ajh6196@psu.edu
#Joe 34

import datetime
import time


class Boil():

    _boil_time = time
    _boil_temp = 0.0
    _stage_date_time = datetime
    _stage_duration = time
    _is_boiling = bool


    def __init__(self):
        self._boil_time
        self._boil_temp
        self._stage_date_time
        self._stage_duration
        self._is_boiling

    def __init__(self, _boil_time, _boil_temp, _stage_date_time, _stage_duration, _is_boiling):
        self._boil_time = _boil_time
        self._boil_temp = _boil_temp
        self._stage_date_time = _stage_date_time
        self._stage_duration = _stage_duration
        self._is_boiling = _is_boiling

    def get_boil_time(self):
        return self._boil_time
    def set_boil_time(self, _boil_time):
        self._boil_time = _boil_time

    def get_boil_temp(self):
        return self._boil_temp
    def set_boil_temp(self, _boil_temp):
        self._boil_temp = _boil_temp

    def get_stage_date_time(self):
        return self._stage_date_time
    def set_stage_date_time(self, _stage_date_time):
        self._stage_date_time = _stage_date_time

    def get_stage_duration(self):
        return self._stage_duration
    def set_stage_duration(self, _stage_duration):
        self._stage_duration = _stage_duration

    def start_boil(self):
        return self.start_boil()

    def update_boil_status(self, _is_boiling):
        self._is_boiling = _is_boiling


