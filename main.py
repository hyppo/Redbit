from MtGox import MtGox
from DataSet import DataSet
from Data import Data
import time
import os


#############################################
# Change the following variables as desired #
#############################################

SELL_THRESHOLD = 20.00    # Bot will sell bitcoins once the sell value goes above this
BUY_THRESHOLD = 15.00     # Bot will buy bitcoins once the buy value goes below this
UPDATE_TIME = 5           # How often the bot retrieves new data in seconds


def main():
  m = MtGox()
  d = DataSet()
  while True:
    m.updateDataSet(d)
    if m.getSell() > SELL_THRESHOLD:
      m.sellBTC(int(m.getBTC()),m.getSell()-0.01)
    if m.getBuy() < BUY_THRESHOLD:
      m.buyBTC(m.getUSD()%m.getBuy(), m.getBuy()+0.01)
    os.system("clear")
    d.printData()
    m.printBTC()
    m.printUSD()
    time.sleep(UPDATE_TIME)



if __name__ == "__main__":
  main()
