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
      r['profilePicture'] = r.pop('avatar_url')
      r['gravatarID'] = r.pop('gravatar_id')
      r.pop('url')
      r['profilePage'] = r.pop('html_url')
      r.pop('starred_url')
      r['lastUpdataed'] = r.pop('updated_at')
      r['isAdmin'] = r.pop('site_admin')
      r['accountCreated'] = r.pop('created_at')
      r['subscriptions'] = r.rop('subscriptions_url') # make sure to do some stuf wif later
    except:
      raise userNotFoundErr("User not found");
  def raw_data(self):
    return self.r