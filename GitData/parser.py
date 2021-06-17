class dictErr(Exception):
  pass
class parse:
  def __init__(self, data):
    if (type(data) != dict):
      dictErr("Not a dict")
    self.r = data
  def raw(self):
    return self.r.raw_data()
  def username(self):
    return self.r.raw_data()['username']


