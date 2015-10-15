from etlcookbook.recipes.uniform_sample import MRUniformSample

class UniformSampleInstance(MRUniformSample):
	def __init__(self, *args, **kwargs):
		super(UniformSampleInstance, self).__init__(*args, **kwargs)
	def groupby(self, line):
		return line["name"]
	def count(self):
		return 2

if __name__=="__main__":
	UniformSampleInstance.run()