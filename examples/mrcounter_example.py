from etlcookbook.recipes.counter import MRCounter

class CounterInstance(MRCounter):
	def __init__(self, *args, **kwargs):
		super(CounterInstance, self).__init__(*args, **kwargs)
	def countby(self, line):
		return line["name"]

if __name__=="__main__":
	CounterInstance.run()