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

  def setStdDevs(self, stdDev):
    self.setHighStdDev(stdDev)
    self.setLowStdDev(stdDev)
    self.setBuyStdDev(stdDev)
    self.setSellStdDev(stdDev)
    self.setVolStdDev(stdDev)
    self.setLastStdDev(stdDev)

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

  def prnt(self, tag, v):
    print "  | %s | %.2f | %.2f | %+.2f |" % (tag, v[0], v[1], v[2])

  def prntVol(self, tag, v):
    print "  | %s | %d | %.2f | %+.2f |" % (tag, v[0], v[1], v[2])

  def printHigh(self):
    self.prnt("High", [self.getHighMean(), self.getHighStdDev(), self.getHighSlope()])

  def printLow(self):
    self.prnt("Low ", [self.getLowMean(), self.getLowStdDev(), self.getLowSlope()])

  def printBuy(self):
    self.prnt("Buy ", [self.getBuyMean(), self.getBuyStdDev(), self.getBuySlope()])

  def printSell(self):
    self.prnt("Sell", [self.getSellMean(), self.getSellStdDev(), self.getSellSlope()])

  def printVol(self):
    self.prntVol("Vol ", [self.getVolMean(), self.getVolStdDev(), self.getVolSlope()])

  def printLast(self):
    self.prnt("Last", [self.getLastMean(), self.getLastStdDev(), self.getLastSlope()])

  def printBar(self):
    print "  |-----------------------------|"

  def printHeader(self):
    self.printBar()
    print "  |      |  Avg  | Stdv | Slope |"
    self.printBar()

  def printData(self):
    self.printHeader()
    self.printBuy()
    self.printSell()
    self.printLast()
    self.printHigh()
    self.printLow()
    self.printVol()
    self.printBar()

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

