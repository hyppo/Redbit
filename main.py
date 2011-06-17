from MtGox import MtGox
from DataSet import DataSet
from Data import Data
import time
import os


#############################################
# Change the following variables as desired #
#############################################

SELL_THRESHOLD = 20.00    # Bot will sell bitcoins once the sell value goes above this
BUY_THRESHOLD = 12.00     # Bot will buy bitcoins once the buy value goes below this
UPDATE_TIME = 2           # How often the bot retrieves new data in seconds
PERCENT_SELL = 0.5        # Percentage of BTC funds to sell when making a sell order
PERCENT_BUY = 0.5         # Percentage of USD funds to buy with when making a buy order 

def main():
  m = MtGox()
  d = DataSet()
  while True:
    m.updateDataSet(d)
    if m.getSell() > SELL_THRESHOLD:
      m.sellBTC(m.getBTC()*PERCENT_SELL,m.getSell())
    if m.getBuy() < BUY_THRESHOLD:
      m.buyBTC((m.getUSD()*PERCENT_BUY)/m.getBuy(), m.getBuy())
    m.updateDataSet(d)
    os.system("clear")
    m.printTitle()
    d.printData()
    m.printFunds()
    m.printOrders()
    m.printStatus()
    time.sleep(UPDATE_TIME)


if __name__ == "__main__":
  main()
