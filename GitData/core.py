import requests
import json
class userNotFoundErr(Exception):
  pass
class dictErr(Exception):
  pass
class readUser():
  def __init__(self, name: str, s = None):
    self.name = name
    if (s == None):
      self.s = None
    else:
      self.s = s
    r =requests.get(f'https://api.github.com/users/{self.name}').json()
    self.r = r
    try:
      r['username'] = r.pop('login') # this renames 'login' which is the users username to 'username'
    except:
      raise userNotFoundErr("User not found");
  def raw_data(self):
    return self.r