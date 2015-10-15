import json
import mrjob
from mrjob.job import MRJob, MRStep

class MRUniformSample(MRJob):
	""" Class to filter json datasets

		count must be overriden (amount = fn() -> int)
		groupby must be overriden
	"""
	OUTPUT_PROTOCOL = mrjob.protocol.RawValueProtocol

	def __init__(self, *args, **kwargs):
		super(MRUniformSample, self).__init__(*args, **kwargs)

	def steps(self):
		return ([
			MRStep(mapper=self.mapper,
					reducer=self.reducer
			)
		])

	def mapper(self, _, line):
		line_dict = json.loads(line)
		yield (self.groupby(line_dict), line_dict)

	def reducer(self, _, lines):
		for _ in xrange(self.count()):
			yield None, json.dumps(lines.next())

	def count(self):
		raise NotImplementedError("A method must be defined which returns the number of counts you want")

	def groupby(self, line_dict):
		raise NotImplementedError("A method must be defined which declares which fields should be used to group instances by")

