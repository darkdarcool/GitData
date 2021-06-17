import requests
import json
class readUser:
  def __init__(self, name: str, s = None):
    self.name = name
    if (s == None):
      self.s = None
    else:
      self.s = s
  def data(self):
    r =requests.get(f'https://api.github.com/users/{self.name}').json()
    r['username'] = r.pop('login') # this renames 'login' which is the users username to 'username'
    return r
