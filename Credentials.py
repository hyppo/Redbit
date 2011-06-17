class Credentials:
  def __init__(self, user, password):
    self.setUser(user)
    self.setPass(password)

  def setUser(self, user):
    self.user = user

  def setPass(self, password):
    self.password = password

  def getUser(self):
    return self.user

  def getPass(self):
    return self.password

