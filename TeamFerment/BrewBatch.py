#Project: IST 440 Barlog Brewery
#Purpose Details: To develop a brew batch class
#Course: IST 440
#Author: Jinal Parmar (fjp5090@psu.edu)
#Date Developed: 3/16/2020
#Last Date Changed: 3/19/2020
#Rev: 1




class BrewBatch:
	def __init__(self, _brew_master_ID, _batch_id,batchStageObj, _batch_duration):

		self._brew_master_ID = _brew_master_ID
		self._batch_id = _batch_id
		self.batchStageObj = batchStageObj
		self._batch_duration = _batch_duration

	def get_BBID(self):
		return self._batch_id

	def get_brew_master_ID(self):
		return self._brew_master_ID

	def get_batch_id(self):
		return self._batch_id

	def get_batch_duration(self):
		return self._batch_duration
