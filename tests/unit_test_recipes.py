from etlcookbook.recipes.filter import MRFilter
from etlcookbook.recipes.counter import MRCounter
from etlcookbook.recipes.uniform_sample import MRUniformSample
from unittest import TestCase

class FilterInstance(MRFilter):
	def __init__(self, *args, **kwargs):
		super(FilterInstance, self).__init__(*args, **kwargs)
	def valid(self, line):
		if line["name"] == "a":
			return True
		return False
	def extract(self, line):
		return {"name":line["name"]}

class CounterInstance(MRCounter):
	def __init__(self, *args, **kwargs):
		super(CounterInstance, self).__init__(*args, **kwargs)

	def groupby(self, line):
		return line["name"]

class UniformSampleInstance(MRUniformSample):
	def __init__(self, *args, **kwargs):
		super(UniformSampleInstance, self).__init__(*args, **kwargs)
	def groupby(self, line):
		return line["name"]
	def count(self):
		return 1

class FilterInstanceTestCase(TestCase):
	def test_filter_valid(self):
		f = FilterInstance()
		self.assertEqual(f.valid({"name": "a"}),True)
		self.assertEqual(f.valid({"name": "b"}),False)
	def test_filter_extract(self):
		f = FilterInstance()
		self.assertEqual(f.extract({"name": "a", "foo":"bar"}),{"name":"a"})
		self.assertEqual(f.extract({"name": "b", "foo":"bar"}),{"name":"b"})

class CounterInstanceTestCase(TestCase):
	def test_counter_groupby(self):
		c = CounterInstance()
		self.assertEqual(c.groupby({"name":"a"}), "a")
		self.assertEqual(c.groupby({"name":"b"}), "b")

class UniformSampleTestCase(TestCase):
	def test_uniform_sample_groupby(self):
		u = UniformSampleInstance()
		self.assertEqual(u.groupby({"name": "a", "foo":"bar"}),"a")
	def test_uniform_sample_count(self):
		u = UniformSampleInstance()
		self.assertEqual(u.count(),1)
