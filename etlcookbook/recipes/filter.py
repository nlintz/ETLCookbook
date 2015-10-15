import json
import mrjob
from mrjob.job import MRJob, MRStep

class MRFilter(MRJob):
	""" Class to filter json datasets

		Valid and Extract must be overridden
	"""
	OUTPUT_PROTOCOL = mrjob.protocol.RawValueProtocol

	def __init__(self, *args, **kwargs):
		super(MRFilter, self).__init__(*args, **kwargs)

	def steps(self):
		return ([
			MRStep(mapper=self.mapper)
		])

	def mapper(self, _, line):
		line_dict = json.loads(line)
		if self.valid(line_dict):
			yield None,json.dumps(self.extract(line_dict))

	def valid(self, line_dict):
		raise NotImplementedError("A method must be defined which declares which objects are valid")

	def extract(self, line_dict):
		raise NotImplementedError("A method must be defined which declares which fields should be returned")


