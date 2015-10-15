import json
import mrjob
from mrjob.job import MRJob, MRStep

class MRCounter(MRJob):
	""" Class to count json instances

		Extract must be overridden
	"""

	def __init__(self, *args, **kwargs):
		super(MRCounter, self).__init__(*args, **kwargs)

	def steps(self):
		return ([
			MRStep(mapper=self.mapper,
					combiner=self.combiner,
					reducer=self.reducer)
		])

	def mapper(self, _, line):
		line_dict = json.loads(line)
		yield (self.countby(line_dict), 1)
	
	def combiner(self, count_field, counts):
		yield (count_field, sum(counts))
	
	def reducer(self, count_field, counts):
		yield(count_field, sum(counts))

	def groupby(self, line_dict):
		raise NotImplementedError("A method must be defined which declares which fields should be used to group instances by")


