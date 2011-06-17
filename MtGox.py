from Credentials import Credentials
import urllib2
import urllib
import time
import contextlib
import math
import datetime
from DataSet import DataSet
from Data import Data

#############################################
# Change the following variables as desired #
#############################################

USERNAME = "CHANGE_ME"      # Mt.Gox username
PASSWORD = "CHANGE_ME"      # Mt.Gox password
DEFAULT_SIMULATION = True   # True = simulation, False = actual trading on Mt.Gox
DEFAULT_BTC = 1             # Starting out amount of BTC (simulation only)
DEFAULT_USD = 50            # Starting out amount of USD (simulation only)
DEFAULT_PRINT = True        # True = output stuff to screen, False = don't output stuff


#########################################
# Don't change the following variables! #
#########################################

BASE_URL = "https://mtgox.com/code/"
TICKER_URL = "data/ticker.php"
MARKET_DEPTH_URL = "data/getDepth.php"
BUY_BTC_URL = "buyBTC.php"
SELL_BTC_URL = "sellBTC.php"
CANCEL_ORDER_URL = "cancelOrder.php"
GET_ORDERS_URL = "getOrders.php"
GET_FUNDS_URL = "getFunds.php"

# Use this class to interact with Mt.Gox API
class MtGox:
  def __init__(self):
    self.credentials = Credentials(USERNAME,PASSWORD)
    self.setBTC(self.getDefaultBTC())
    self.setUSD(self.getDefaultUSD())
    self.setPrint(self.getDefaultPrint())    
    self.setSimulation(self.getDefaultSimulation())
    self.update()


  def printStatus(self):
    if self.getSimulation():
      print "                    Status:  Simulation"
    else:
      print "                    Status:   Live"
      print "                    Username: %s" % self.getUser()  

  def printTitle(self):
    print "              Mt.Gox @ %s" % datetime.datetime.now().strftime("%H:%M:%S on %m/%d/%Y")

  # Get default simulation value
  def getDefaultSimulation(self):
    return DEFAULT_SIMULATION

  # Get current simulation value
  def getSimulation(self):
    return self.simulation

  # Set simulation value (True = simulation, False = real deal)
  def setSimulation(self, simulation):
    self.simulation = simulation

  # Set the print boolean (True = output to screen, False = don't output)
  def setPrint(self, prnt):
    self.canPrint = prnt

  # Get default BTC amount (only relevant for simulation)
  def getDefaultBTC(self):
    return DEFAULT_BTC

  # Get default USD amount (only relevant for simulation)
  def getDefaultUSD(self):
    return DEFAULT_USD

  # Get default print boolean value
  def getDefaultPrint(self):
    return DEFAULT_PRINT

  # Set BTC amount (only relevant to simulation)
  def setBTC(self, btc):
    self.btc = btc

  # Get your BTC fund amount
  def getBTC(self):
    return self.btc

  # Set USD amount (only relevant to simulation)
  def setUSD(self, usd):
    self.usd = usd

  # Get you USD fund amount
  def getUSD(self):
    return self.usd

  # Set your credentials (requires a Credential class instance)
  def setCredentials(self, credentials):
    self.credentials = credentials

  # Get credentials (Credentials class instance)
  def getCredentials(self):
    return self.credentials

  # Get username
  def getUser(self):
    return self.getCredentials().getUser()

  # Get password
  def getPass(self):
    return self.getCredentials().getPass()

  # Set username
  def setUser(self, user):
    return self.getCredentials().setUser(user)

  # Set password
  def setPass(self, password):
    return self.getCredentials().setPass(password)

  # Buy "btc" many BTCs each for "price" amount
  def buyBTC(self, btc, price):
    if self.canBuy(btc, price):
      self.printBuyMsg(btc, price)
      if self.getSimulation():
        self.deductUSD(price * btc)
        self.addBTC(btc)
      else: 
        self.getURLWithParams(BUY_BTC_URL, {'amount':btc,'price':price})
    else:
      self.prnt("Do not have enough USD to submit order for %.2f BTC @ %.2f USD a piece" % (btc, price))

  # Deduct USD from funds (simulation)
  def deductUSD(self, usd):
    if self.getSimulation():
      self.usd -= usd
    else:
      self.prnt("This is not a simulation.  Cannot deduct USD.")

  # Deduct BTC from funds (simulation)
  def deductBTC(self, btc):
    if self.getSimulation():
      self.btc -= btc
    else:
      self.prnt("This is not a simulation.  Cannot deduct BTC.")

  # Add USD funds (simulation)
  def addUSD(self, usd):
    if self.getSimulation():
      self.usd += usd
    else:
      self.prnt("This is not a simulation.  Cannot add USD.")

  # Add BTC funds (simulation)
  def addBTC(self, btc):
    if self.getSimulation():
      self.btc += btc
    else:
      self.prnt("This is not a simulation.  Cannot add BTC.")

  # Check if printing is on (True = print to screen, False = don't print to screen)
  def printingOn(self):
    return self.canPrint

  # Prints the buying message
  def printBuyMsg(self, btc, price):
    self.prnt("Buying " + str(btc) + " BTC for " + str(price) + " USD each (Total = " + str(btc * price) + " USD)")

  # Checks to see if enough funds are available to proceed with the proposed purchase
  def canBuy(self, btc, usd):
    return self.getUSD() >= (btc * usd)

  # Sell "btc" many BTCs each for "price" amount
  def sellBTC(self, btc, price):
    if self.canSell(btc):
      self.printSellMsg(btc, price)
      if self.getSimulation():
        self.deductBTC(btc)
        self.addUSD(btc * price)
      else:
        self.getURLWithParams(SELL_BTC_URL, {'amount':btc,'price':price})
    else:
      self.prnt("Do not have enough BTC to submit sell order for %.2f BTC @ %.2f USD a piece" % (btc, price))

  # Prints the selling message
  def printSellMsg(self, btc, price):
      self.prnt("Selling " + str(btc) + " BTC for " + str(price) + " USD each (Total = " + str(btc * price) + " USD)")

  # Checks to see if there are enough BTC funds to proceed with the sell
  def canSell(self, btc):
    return self.getBTC() >= btc

  def updateDataSet(self, d):
    self.update()
    d.addData(self.getNewData())

  def getNewData(self):
    return Data(self.getUSD(), self.getBTC(), self.getHigh(), self.getLow(), self.getLast(), self.getVol(), self.getBuy(), self.getSell(), \
                self.getTotalAskPrice(), self.getTotalAskVolume(), self.getAvgAskPrice(), \
                self.getTotalBidPrice(), self.getTotalBidVolume(), self.getAvgBidPrice())

  # Update data values from Mt.Gox (it's important to do this often to keep values current)
  def update(self):
    tickerData = self.getTickerData()
    self.setLast(tickerData['last'])
    self.setSell(tickerData['sell'])
    self.setBuy(tickerData['buy'])
    self.setVol(tickerData['vol'])
    self.setLow(tickerData['low'])
    self.setHigh(tickerData['high'])
    
    if self.getSimulation() == False:
      funds = self.getFunds()
      self.setBTC(funds['btcs'])
      self.setUSD(funds['usds'])
    
    self.setOrders(self.getOrdersData())
    
    marketDepth = self.getMarketDepth()
    self.setAsks(marketDepth['asks'])
    self.setBids(marketDepth['bids'])


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

  def setAsks(self, asks):
    self.setTotalAskPrice(sum([x[0]*x[1] for x in asks]))
    self.setTotalAskVolume(sum([x[1] for x in asks]))
    self.setAvgAskPrice(float(self.totalAskPrice)/float(self.totalAskVolume))

  def setBids(self, bids):
    self.setTotalBidPrice(sum([x[0]*x[1] for x in bids]))
    self.setTotalBidVolume(sum([x[1] for x in bids]))
    self.setAvgBidPrice(float(self.totalBidPrice)/float(self.totalBidVolume))

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


  # Get funds from Mt.Gox
  def getFunds(self):
    return self.getURL(GET_FUNDS_URL)

  def printFunds(self):
    self.printBTC()
    self.printUSD()
    self.printSeperator()

  def addSpaces(self, base, value, delta):
    if int(value) == 0:
      dec = 0
    else:
      dec = int(math.log(int(value),10))
    for i in range(20 - dec + delta):
      base += " "
    return base + "|"

  # Print BTC funds
  def printBTC(self):
    self.prnt(self.addSpaces("  |                    BTC:  %.2f" % self.getBTC(), self.getBTC(), -1))

  # Print USD funds
  def printUSD(self):
    self.prnt(self.addSpaces("  |                    USD:  %.2f" % self.getUSD(), self.getUSD(), -1))

  # Print high
  def printHigh(self):
    self.prnt("High: " + str(self.getHigh()))

  # Print low
  def printLow(self):
    self.prnt("Low:  " + str(self.getLow()))

  # Print last
  def printLast(self):
    self.prnt("Last: " + str(self.getLast()))

  # Print volume
  def printVol(self):
    self.prnt("Vol:  " + str(self.getVol()))

  # Print buy
  def printBuy(self):
    self.prnt("Buy:  " + str(self.getBuy()))
  
  # Print sell
  def printSell(self):
    self.prnt("Sell: " + str(self.getSell()))

  # Print a message
  def prnt(self, string):
    if self.printingOn():
      print string

  # Print Mt.Gox data
  def printData(self):
    self.printLast()
    self.printBuy()
    self.printSell()
    self.printHigh()
    self.printLow()
    self.printVol()

  # Get last
  def getLast(self):
    return self.last

  # Set last
  def setLast(self, last):
    self.last = last

  # Get sell
  def getSell(self):
    return self.sell

  # Set sell
  def setSell(self, sell):
    self.sell = sell

  # Get buy
  def getBuy(self):
    return self.buy

  # Set buy
  def setBuy(self, buy):
    self.buy = buy

  # Get volume
  def getVol(self):
    return self.vol

  # Set volume
  def setVol(self, vol):
    self.vol = vol

  # Get low
  def getLow(self):
    return self.low

  # Set low
  def setLow(self, low):
    self.low = low

  # Get high (/r/trees)
  def getHigh(self):
    return self.high

  # Set high
  def setHigh(self, high):
    self.high = high

  # Get ticker data from Mt.Gox
  def getTickerData(self):
    return self.getPlainURL(TICKER_URL)['ticker']

  def getMarketDepth(self):
    return self.getPlainURL(MARKET_DEPTH_URL)

  # Get data from URL without using credentials
  def getPlainURL(self, url):
    url = BASE_URL + url
    f = urllib2.urlopen(url)
    data = eval(f.read())
    contextlib.closing(f)
    return data

  # Get data from URL using credentials
  def getURL(self, url):
    url = BASE_URL + url
    f = urllib2.urlopen(url,self.getEncodedCreds())
    data = eval(f.read())
    contextlib.closing(f)
    return data

  # Get data from URL with extra parameters
  def getURLWithParams(self, url, dict):
    url = BASE_URL + url
    dict.update(self.getCredsDict())
    f = urllib2.urlopen(url,self.getURLEncoded(dict))
    data = eval(f.read())
    contextlib.closing(f)
    return data

  # Get URL encoded credentials
  def getEncodedCreds(self):
    return self.getURLEncoded(self.getCredsDict())

  # Get URL encoded version of parameter dictionary
  def getURLEncoded(self, dict):
    return urllib.urlencode(dict)

  # Get credentials dictionary
  def getCredsDict(self):
    return {'name': self.getCredentials().getUser(), 'pass': self.getCredentials().getPass()}

  def cancelOrder(self, oid):
    order = self.getOrder(oid)
    if order == None:
      return
    return self.getURLWithParams(CANCEL_ORDER_URL, {'oid':order['oid'],'type':order['type']})

  def getOrder(self, oid):
    if self.getSimulation():
      return None
    for order in self.getOrders():
      if order['oid'] == oid:
        return order
    return None

  def getNumOrders(self):
    return len(self.getOrders())    

  def getOrders(self):
    return self.orders

  def setOrders(self, orders):
    self.orders = orders

  def getOrdersData(self):
    if self.getSimulation():
      return []
    return self.getURL(GET_ORDERS_URL)['orders']

  def printBar(self):
    print "  |-------------------------------------------------|"

  def printSeperator(self):
    print "  |=================================================|"

  def printNoOrders(self):
    print "  |                 No orders placed                |"

  def printOrders(self):
    self.printOrderHeader()
    self.printBar()
    if self.getNumOrders() == 0:
      self.printNoOrders()
    else:
      for order in self.getOrders():
        self.printOrder(order)
    self.printSeperator()

  def printOrderHeader(self):
    print "  |      OID       |     Type      |     Status     |"

  def printOrder(self, order):
    oid = order['oid']
    if str(order['type']) == '1':
      type = "sell"
    else:
      type = "buy "
    if order['status'] == '1':
      status = "active"
    else:
      status = " NSF  "
    print self.addSpaces("  |     %s" % oid, oid, -10) + "     %s      |     %s     |" % (type, status)

if __name__ == '__main__':
  main()
