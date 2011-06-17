class Data:
  def __init__(self, usd, btc, high, low, last, vol, buy, sell, totalAskPrice, totalAskVolume, avgAskPrice, totalBidPrice, totalBidVolume, avgBidPrice):
    self.setUSD(usd)
    self.setBTC(btc)
    self.setHigh(high)
    self.setLow(low)
    self.setLast(last)
    self.setVol(vol)
    self.setBuy(buy)
    self.setSell(sell)
    self.setTotalAskPrice(totalAskPrice)
    self.setTotalAskVolume(totalAskVolume)
    self.setAvgAskPrice(avgAskPrice)
    self.setTotalBidPrice(totalBidPrice)
    self.setTotalBidVolume(totalBidVolume)
    self.setAvgBidPrice(avgBidPrice)

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

  def setTotalAskPrice(self, totalAskPrice):
    self.totalAskPrice = totalAskPrice
 
  def setTotalAskVolume(self, totalAskVolume):
    self.totalAskVolume = totalAskVolume

  def setAvgAskPrice(self, avgAskPrice):
    self.avgAskPrice = avgAskPrice

  def getTotalAskPrice(self):
    return self.totalAskPrice

  def getTotalAskVolume(self):
    return self.totalAskVolume

  def getAvgAskPrice(self):
    return self.avgAskPrice

  def setTotalBidPrice(self, totalBidPrice):
    self.totalBidPrice = totalBidPrice

  def setTotalBidVolume(self, totalBidVolume):
    self.totalBidVolume = totalBidVolume

  def setAvgBidPrice(self, avgBidPrice):
    self.avgBidPrice = avgBidPrice

  def getTotalBidPrice(self):
    return self.totalBidPrice

  def getTotalBidVolume(self):
    return self.totalBidVolume

  def getAvgBidPrice(self):
    return self.avgBidPrice

