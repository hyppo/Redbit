class Data:
  def __init__(self, usd, btc, high, low, last, vol, buy, sell):
    self.setUSD(usd)
    self.setBTC(btc)
    self.setHigh(high)
    self.setLow(low)
    self.setLast(last)
    self.setVol(vol)
    self.setBuy(buy)
    self.setSell(sell)

  def setBTC(self, btc):
    self.btc = btc

  def getBTC(self):
    return self.btc

  def setUSD(self, usd):
    self.usd = usd

  def getUSD(self):
    return self.usd

  def setHigh(self, high):
    self.high = high

  def getHigh(self):
    return self.high

  def setLow(self, low):
    self.low = low

  def getLow(self):
    return self.low

  def setLast(self, last):
    self.last = last

  def getVol(self):
    return self.vol

  def setVol(self, vol):
    self.vol = vol

  def getLast(self):
    return self.last

  def setBuy(self, buy):
    self.buy = buy

  def getBuy(self):
    return self.buy

  def setSell(self, sell):
    self.sell = sell

  def getSell(self):
    return self.sell

