from etlcookbook.recipes.filter import MRFilter

class FilterInstance(MRFilter):
  def __init__(self, *args, **kwargs):
    super(FilterInstance, self).__init__(*args, **kwargs)
  def valid(self, line):
    if line["name"] == "a":
      return True
    return False
  def extract(self, line):
    return {"name":line["name"]}

if __name__=="__main__":
  FilterInstance.run()