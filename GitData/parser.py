class dictErr(Exception):
  pass
class parse:
  def __init__(self, data):
    if (type(data) != dict):
      raise dictErr("Not a dict")
    self.r = data
  def raw(self):
    return self.r.raw_data()
  def username(self):
    return self.r.raw_data()['username']
  def id(self):
    return self.r.raw_data()['id']
  def node_id(self):
    return self.r.raw_data()['node_id']
  def followers_url(self):
    return self.r.raw_data()['followers_url']
  def following_url(self):
    return self.r.raw_data()['following_url']
  def gists_url(self):
    return self.r.raw_data()['gists_url']
  def subscriptions(self):
    return self.r.raw_data()['subscriptions']
