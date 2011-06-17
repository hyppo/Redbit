import math
from Data import Data

DEFAULT_MEAN = -1
DEFAULT_STDDEV = -1
DEFAULT_SLOPE = 0
DEFAULT_MAX_DATA = 5
DEFAULT_DECIMAL_PLACES = 4

UNDEFINED_SLOPE = 0

class DataSet:
  def __init__(self):
    self.resetData()
    self.setMeans(DEFAULT_MEAN)
    self.setStdDevs(DEFAULT_STDDEV)
    self.setSlopes(DEFAULT_SLOPE)    
    self.setMaxData(DEFAULT_MAX_DATA)

  def setMeans(self, mean):
    self.setHighMean(mean)
    self.setLowMean(mean)
    self.setBuyMean(mean)
    self.setSellMean(mean)
    self.setVolMean(mean)
    self.setLastMean(mean)
    self.setTotalAskPriceMean(mean)
    self.setTotalAskVolumeMean(mean)
    self.setAvgAskPriceMean(mean)

  def setMaxData(self, maxData):
    self.maxData = maxData

  def getMaxData(self):
    return self.maxData

  def setHighMean(self, highMean):
    self.highMean = highMean

  def setLowMean(self, lowMean):
    self.lowMean = lowMean

  def setBuyMean(self, buyMean):
    self.buyMean =  buyMean
 
  def setSellMean(self, sellMean):
    self.sellMean = sellMean

  def setVolMean(self, volMean):
    self.volMean = volMean

  def setLastMean(self, lastMean):
    self.lastMean = lastMean

  def getHighMean(self):
    return self.highMean

  def getLowMean(self):
    return self.lowMean

  def getBuyMean(self):
    return self.buyMean
 
  def getSellMean(self):
    return self.sellMean

  def getVolMean(self):
    return self.volMean

  def getLastMean(self):
    return self.lastMean

  def getTotalAskPriceMean(self):
    return self.totalAskPriceMean

  def getTotalAskVolumeMean(self):
    return self.totalAskVolumeMean

  def getAvgAskPriceMean(self):
    return self.avgAskPriceMean

  def getTotalBidPriceMean(self):
    return self.totalBidPriceMean

  def getTotalBidVolumeMean(self):
    return self.totalBidVolumeMean

  def getAvgBidPriceMean(self):
    return self.avgBidPriceMean

  def setTotalAskPriceMean(self, totalAskPriceMean):
    self.totalAskPriceMean = totalAskPriceMean

  def setTotalAskVolumeMean(self, totalAskVolumeMean):
    self.totalAskVolumeMean = totalAskVolumeMean

  def setAvgAskPriceMean(self, avgAskPriceMean):
    self.avgAskPriceMean = avgAskPriceMean

  def setTotalBidPriceMean(self, totalBidPriceMean):
    self.totalBidPriceMean = totalBidPriceMean

  def setTotalBidVolumeMean(self, totalBidVolumeMean):
    self.totalBidVolumeMean = totalBidVolumeMean

  def setAvgBidPriceMean(self, avgBidPriceMean):
    self.avgBidPriceMean = avgBidPriceMean


  def setStdDevs(self, stdDev):
    self.setHighStdDev(stdDev)
    self.setLowStdDev(stdDev)
    self.setBuyStdDev(stdDev)
    self.setSellStdDev(stdDev)
    self.setVolStdDev(stdDev)
    self.setLastStdDev(stdDev)
    self.setTotalAskPriceStdDev(stdDev)
    self.setTotalAskVolumeStdDev(stdDev)
    self.setAvgAskPriceStdDev(stdDev)

  def getTotalAskPriceStdDev(self):
    return self.totalAskPriceStdDev

  def getTotalAskVolumeStdDev(self):
    return self.totalAskVolumeStdDev

  def getAvgAskPriceStdDev(self):
    return self.avgAskPriceStdDev

  def setTotalAskPriceStdDev(self, totalAskPriceStdDev):
    self.totalAskPriceStdDev = totalAskPriceStdDev

  def setTotalAskVolumeStdDev(self, totalAskVolumeStdDev):
    self.totalAskVolumeStdDev = totalAskVolumeStdDev

  def setAvgAskPriceStdDev(self, avgAskPriceStdDev):
    self.avgAskPriceStdDev = avgAskPriceStdDev

  def getTotalBidPriceStdDev(self):
    return self.totalBidPriceStdDev

  def getTotalBidVolumeStdDev(self):
    return self.totalBidVolumeStdDev

  def getAvgBidPriceStdDev(self):
    return self.avgBidPriceStdDev

  def setTotalBidPriceStdDev(self, totalBidPriceStdDev):
    self.totalBidPriceStdDev = totalBidPriceStdDev

  def setTotalBidVolumeStdDev(self, totalBidVolumeStdDev):
    self.totalBidVolumeStdDev = totalBidVolumeStdDev

  def setAvgBidPriceStdDev(self, avgBidPriceStdDev):
    self.avgBidPriceStdDev = avgBidPriceStdDev

  def setHighStdDev(self, highStdDev):
    self.highStdDev = highStdDev

  def setLowStdDev(self, lowStdDev):
    self.lowStdDev = lowStdDev

  def setBuyStdDev(self, buyStdDev):
    self.buyStdDev = buyStdDev
 
  def setSellStdDev(self, sellStdDev):
    self.sellStdDev = sellStdDev

  def setVolStdDev(self, volStdDev):
    self.volStdDev = volStdDev

  def setLastStdDev(self, lastStdDev):
    self.lastStdDev = lastStdDev

  def getHighStdDev(self):
    return self.highStdDev

  def getLowStdDev(self):
    return self.lowStdDev

  def getBuyStdDev(self):
    return self.buyStdDev
 
  def getSellStdDev(self):
    return self.sellStdDev

  def getVolStdDev(self):
    return self.volStdDev

  def getLastStdDev(self):
    return self.lastStdDev

  def setSlopes(self, slope):
    self.setHighSlope(slope)
    self.setLowSlope(slope)
    self.setBuySlope(slope)
    self.setSellSlope(slope)
    self.setVolSlope(slope)
    self.setLastSlope(slope)
    self.setTotalAskPriceSlope(slope)
    self.setTotalAskVolumeSlope(slope)
    self.setAvgAskPriceSlope(slope)

  def getTotalAskPriceSlope(self):
    return self.totalAskPriceSlope

  def getTotalAskVolumeSlope(self):
    return self.totalAskVolumeSlope

  def getAvgAskPriceSlope(self):
    return self.avgAskPriceSlope

  def setTotalAskPriceSlope(self, totalAskPriceSlope):
    self.totalAskPriceSlope = totalAskPriceSlope

  def setTotalAskVolumeSlope(self, totalAskVolumeSlope):
    self.totalAskVolumeSlope = totalAskVolumeSlope

  def setAvgAskPriceSlope(self, avgAskPriceSlope):
    self.avgAskPriceSlope = avgAskPriceSlope

  def getTotalBidPriceSlope(self):
    return self.totalBidPriceSlope

  def getTotalBidVolumeSlope(self):
    return self.totalBidVolumeSlope

  def getAvgBidPriceSlope(self):
    return self.avgBidPriceSlope

  def setTotalBidPriceSlope(self, totalBidPriceSlope):
    self.totalBidPriceSlope = totalBidPriceSlope

  def setTotalBidVolumeSlope(self, totalBidVolumeSlope):
    self.totalBidVolumeSlope = totalBidVolumeSlope

  def setAvgBidPriceSlope(self, avgBidPriceSlope):
    self.avgBidPriceSlope = avgBidPriceSlope

  def setHighSlope(self, highSlope):
    self.highSlope = highSlope

  def setLowSlope(self, lowSlope):
    self.lowSlope = lowSlope

  def setBuySlope(self, buySlope):
    self.buySlope = buySlope
 
  def setSellSlope(self, sellSlope):
    self.sellSlope = sellSlope

  def setVolSlope(self, volSlope):
    self.volSlope = volSlope

  def setLastSlope(self, lastSlope):
    self.lastSlope = lastSlope

  def getHighSlope(self):
    return self.highSlope

  def getLowSlope(self):
    return self.lowSlope

  def getBuySlope(self):
    return self.buySlope
 
  def getSellSlope(self):
    return self.sellSlope

  def getVolSlope(self):
    return self.volSlope

  def getLastSlope(self):
    return self.lastSlope

  def empty(self):
    return self.dataCount == 0

  def getDataCount(self):
    return len(self.getData())

  def getData(self):
    return self.data

  def resetData(self):
    if hasattr(self, 'data'):
      del self.data[:]
    else:
      self.data = []

  def setData(self, data):
    self.data = data

  def addData(self, data):
    self.data.append(data)
    if self.getDataCount() > self.getMaxData():
      self.truncData()
    self.doCalcs()

  def truncData(self):
    self.setData(self.getData()[1:])

  def doCalcs(self):
    self.calcMeans()
    self.calcStdDevs()
    self.calcSlopes()

  def calcMeans(self):
    self.calcHighMean()
    self.calcLowMean()
    self.calcBuyMean()
    self.calcSellMean()
    self.calcVolMean()
    self.calcLastMean()
    self.calcTotalAskPriceMean()
    self.calcTotalAskVolumeMean()
    self.calcAvgAskPriceMean()
    self.calcTotalBidPriceMean()
    self.calcTotalBidVolumeMean()
    self.calcAvgBidPriceMean()

  def calcTotalAskPriceMean(self):
    self.setTotalAskPriceMean(self.getMean([x.getTotalAskPrice() for x in self.getData()]))

  def calcTotalAskVolumeMean(self):
    self.setTotalAskVolumeMean(self.getMean([x.getTotalAskVolume() for x in self.getData()]))

  def calcAvgAskPriceMean(self):
    self.setAvgAskPriceMean(self.getMean([x.getAvgAskPrice() for x in self.getData()]))

  def calcTotalBidPriceMean(self):
    self.setTotalBidPriceMean(self.getMean([x.getTotalBidPrice() for x in self.getData()]))

  def calcTotalBidVolumeMean(self):
    self.setTotalBidVolumeMean(self.getMean([x.getTotalBidVolume() for x in self.getData()]))

  def calcAvgBidPriceMean(self):
    self.setAvgBidPriceMean(self.getMean([x.getAvgBidPrice() for x in self.getData()]))

  def calcHighMean(self):
    self.setHighMean(self.getMean([x.getHigh() for x in self.getData()]))

  def calcLowMean(self):
    self.setLowMean(self.getMean([x.getLow() for x in self.getData()]))

  def calcBuyMean(self):
    self.setBuyMean(self.getMean([x.getBuy() for x in self.getData()]))

  def calcSellMean(self):
    self.setSellMean(self.getMean([x.getSell() for x in self.getData()]))

  def calcVolMean(self):
    self.setVolMean(self.getMean([x.getVol() for x in self.getData()]))

  def calcLastMean(self):
    self.setLastMean(self.getMean([x.getLast() for x in self.getData()]))

  def getMean(self, values):
    return float(sum(values))/len(values)

  def calcStdDevs(self):
    self.calcHighStdDev()
    self.calcLowStdDev()
    self.calcBuyStdDev()
    self.calcSellStdDev()
    self.calcVolStdDev()
    self.calcLastStdDev()
    self.calcTotalAskPriceStdDev()
    self.calcTotalAskVolumeStdDev()
    self.calcAvgAskPriceStdDev()
    self.calcTotalBidPriceStdDev()
    self.calcTotalBidVolumeStdDev()
    self.calcAvgBidPriceStdDev()

  def calcTotalAskPriceStdDev(self):
    self.setTotalAskPriceStdDev(self.getStdDev([x.getTotalAskPrice() for x in self.getData()]))

  def calcTotalAskVolumeStdDev(self):
    self.setTotalAskVolumeStdDev(self.getStdDev([x.getTotalAskVolume() for x in self.getData()]))

  def calcAvgAskPriceStdDev(self):
    self.setAvgAskPriceStdDev(self.getStdDev([x.getAvgAskPrice() for x in self.getData()]))

  def calcTotalBidPriceStdDev(self):
    self.setTotalBidPriceStdDev(self.getStdDev([x.getTotalBidPrice() for x in self.getData()]))

  def calcTotalBidVolumeStdDev(self):
    self.setTotalBidVolumeStdDev(self.getStdDev([x.getTotalBidVolume() for x in self.getData()]))

  def calcAvgBidPriceStdDev(self):
    self.setAvgBidPriceStdDev(self.getStdDev([x.getAvgBidPrice() for x in self.getData()]))

  def calcHighStdDev(self):
    self.setHighStdDev(self.getStdDev([x.getHigh() for x in self.getData()]))

  def calcLowStdDev(self):
    self.setLowStdDev(self.getStdDev([x.getLow() for x in self.getData()]))

  def calcBuyStdDev(self):
    self.setBuyStdDev(self.getStdDev([x.getBuy() for x in self.getData()]))

  def calcSellStdDev(self):
    self.setSellStdDev(self.getStdDev([x.getSell() for x in self.getData()]))

  def calcVolStdDev(self):
    self.setVolStdDev(self.getStdDev([x.getVol() for x in self.getData()]))

  def calcLastStdDev(self):
    self.setLastStdDev(self.getStdDev([x.getLast() for x in self.getData()]))

  def getStdDev(self, values):
    mean = self.getMean(values)
    return math.sqrt(sum((x-mean)**2 for x in values)/len(values))
  
  def calcSlopes(self):
    self.calcHighSlope()
    self.calcLowSlope()
    self.calcBuySlope()
    self.calcSellSlope()
    self.calcVolSlope()
    self.calcLastSlope()
    self.calcTotalBidPriceSlope()
    self.calcTotalBidVolumeSlope()
    self.calcAvgBidPriceSlope()

  def calcTotalAskPriceSlope(self):
    self.setTotalAskPriceSlope(self.getSlope([x.getTotalAskPrice() for x in self.getData()]))

  def calcTotalAskVolumeSlope(self):
    self.setTotalAskVolumeSlope(self.getSlope([x.getTotalAskVolume() for x in self.getData()]))

  def calcAvgAskPriceSlope(self):
    self.setAvgAskPriceSlope(self.getSlope([x.getAvgAskPrice() for x in self.getData()]))

  def calcTotalBidPriceSlope(self):
    self.setTotalBidPriceSlope(self.getSlope([x.getTotalBidPrice() for x in self.getData()]))

  def calcTotalBidVolumeSlope(self):
    self.setTotalBidVolumeSlope(self.getSlope([x.getTotalBidVolume() for x in self.getData()]))

  def calcAvgBidPriceSlope(self):
    self.setAvgBidPriceSlope(self.getSlope([x.getAvgBidPrice() for x in self.getData()]))

  def calcHighSlope(self):
    self.setHighSlope(self.getSlope([x.getHigh() for x in self.getData()]))

  def calcLowSlope(self):
    self.setLowSlope(self.getSlope([x.getLow() for x in self.getData()]))

  def calcBuySlope(self):
    self.setBuySlope(self.getSlope([x.getBuy() for x in self.getData()]))

  def calcSellSlope(self):
    self.setSellSlope(self.getSlope([x.getSell() for x in self.getData()]))

  def calcVolSlope(self):
    self.setVolSlope(self.getSlope([x.getVol() for x in self.getData()]))

  def calcLastSlope(self):
    self.setLastSlope(self.getSlope([x.getLast() for x in self.getData()]))

  def getSlope(self, values):
    points = []
    for i in range(len(values)):
      points.append({'x':i, 'y':values[i]})
    n = len(values)
    sx = sum([x['x'] for x in points])
    sy = sum([x['y'] for x in points])
    sxy = sum([x['x']*x['y'] for x in points])
    sxx = sum([x['x']*x['x'] for x in points])
    delta = (n*sxx)-(sx**2)
    if delta == 0:
      return UNDEFINED_SLOPE
    return ((n*sxy)-(sx*sy))/delta

  def prnt(self, tag, v, delta):
    print self.addSpaces(self.addSpaces(self.addSpaces("  | %s | %.2f" % (tag, v[0]), v[0], delta) + (" %.2f" % (v[1])), v[1], delta) + (" %+.2f" % (v[2])), v[2], delta)
  
  def prntVol(self, tag, v, delta1, delta2, delta3):
    print self.addSpaces(self.addSpaces(self.addSpaces("  | %s | %d" % (tag, v[0]), v[0], delta1) + (" %.2f" % (v[1])), v[1], delta2) + (" %+.2f" % (v[2])), v[2], delta3)

  def prntDepth(self, tag, v, delta):
    print self.addSpaces(self.addSpaces(self.addSpaces("  | %s | %d" % (tag, v[0]), v[0], delta) + (" %d" % (v[1])), v[1], delta) + (" %+d" % (v[2])), v[2], delta)

  def addSpaces(self, base, value, delta):
    if int(value) == 0:
      dec = 0
    else:
      if value < 0:
        dec = int(math.log(int(-1*value),10))
      else:
        dec = int(math.log(int(value),10))
    for i in range(delta - dec):
      base += " "
    return base + "|"

  def printHigh(self):
    self.prnt("High            ", [self.getHighMean(), self.getHighStdDev(), self.getHighSlope()], 4)

  def printLow(self):
    self.prnt("Low             ", [self.getLowMean(), self.getLowStdDev(), self.getLowSlope()], 4)

  def printBuy(self):
    self.prnt("Buy             ", [self.getBuyMean(), self.getBuyStdDev(), self.getBuySlope()], 4)

  def printSell(self):
    self.prnt("Sell            ", [self.getSellMean(), self.getSellStdDev(), self.getSellSlope()], 4)

  def printVol(self):
    self.prntVol("Vol             ", [self.getVolMean(), self.getVolStdDev(), self.getVolSlope()], 7, 4, 4)

  def printLast(self):
    self.prnt("Last            ", [self.getLastMean(), self.getLastStdDev(), self.getLastSlope()], 4)

  def printTotalAskPrice(self):
    self.prntDepth("Total Ask Price ", [self.getTotalAskPriceMean(), self.getTotalAskPriceStdDev(), self.getTotalAskPriceSlope()], 7)

  def printTotalAskVolume(self):
    self.prntDepth("Total Ask Volume", [self.getTotalAskVolumeMean(), self.getTotalAskVolumeStdDev(), self.getTotalAskVolumeSlope()], 7)

  def printAvgAskPrice(self):
    self.prnt("Avg Ask Price   ", [self.getAvgAskPriceMean(), self.getAvgAskPriceStdDev(), self.getAvgAskPriceSlope()], 4)

  def printTotalBidPrice(self):
    self.prntDepth("Total Bid Price ", [self.getTotalBidPriceMean(), self.getTotalBidPriceStdDev(), self.getTotalBidPriceSlope()], 7)

  def printTotalBidVolume(self):
    self.prntDepth("Total Bid Volume", [self.getTotalBidVolumeMean(), self.getTotalBidVolumeStdDev(), self.getTotalBidVolumeSlope()], 7)

  def printAvgBidPrice(self):
    self.prnt("Avg Bid Price   ", [self.getAvgBidPriceMean(), self.getAvgBidPriceStdDev(), self.getAvgBidPriceSlope()], 4)

  def printBar(self):
    print "  |-------------------------------------------------|"

  def printSeperator(self):
    print "  |=================================================|"

  def printHeader(self):
    self.printSeperator()
    print "  |                  |   Avg   |  Stdev  |  Slope   |"
    self.printBar()

  def printData(self):
    self.printHeader()
    self.printBuy()
    self.printSell()
    self.printLast()
    self.printHigh()
    self.printLow()
    self.printVol()
    self.printAvgAskPrice()
    self.printTotalAskVolume()
    self.printTotalAskPrice()
    self.printAvgBidPrice()
    self.printTotalBidVolume()
    self.printTotalBidPrice()
    self.printSeperator()

    #correlation coefficients
#    a = []
#    for i in range(len(values)):
#      a.append({'x':i, 'y':values[i]})
#    n = len(values)
#    b = sum([x['x']*x['y'] for x in a])
#    c = sum([x['x'] for x in a])
#    d = sum([x['y'] for x in a])
#    e = sum([x['x']**2 for x in a])
#    f = sum([x['y']**2 for x in a])
#    g = c**2
#    h = d**2
#    return (n*b-c*d)/(math.sqrt(n*e-g)*math.sqrt(n*f-h))

