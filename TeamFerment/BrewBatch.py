# Project: IST 440 Barlog Brewery
# Purpose Details: To develop a brew batch class
# Course: IST 440
# Author: Team Ferment
# Date Developed: 3/16/2020
# Last Date Changed: 4/1/2020
# Rev: 2

class BrewBatch:
	"""
	This class has been written to provide the Brew Master with information regarding the BrewBatch attributes
	"""
	def __init__(self, _brew_master_ID, _batch_id, batchStageObj, _batch_duration):

		self._brew_master_ID = _brew_master_ID
		self._batch_id = _batch_id
		self.batchStageObj = batchStageObj
		self._batch_duration = _batch_duration

	def get_BBID(self):
		"""
		:return: BrewBatch ID
		This provides BBID to distinguish the Brew Batch
		"""
		return self._batch_id

	def get_brew_master_ID(self):
		"""
		:return: Brew Master ID
		This provides the Brew Master's ID, giving information pertaining to their corresponding Brew Batch
		"""
		return self._brew_master_ID

	def get_batch_id(self):
		"""
		:return: Brew Batch ID
		"""
		return self._batch_id

	def get_batch_duration(self):
		"""
		:return: Batch Duration
		This provides the Brew Master with the remaining time left in the Lager's brewing.
		"""
		return self._batch_duration
