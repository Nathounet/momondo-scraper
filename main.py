### Libraries
import platform, sys
from time import sleep
from copy import deepcopy
from pprint import pprint
from datetime import datetime
from selenium import webdriver
from ConfigParser import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Custom modules
from date_time import Date, Time
from flight import Flight
from url import URL

### Parameters
path_config_file = './search.conf'
if platform.system() == 'Darwin':
    path_to_chromedriver = './webdriver/chromedriver'
elif platform.system() == 'Windows':
    path_to_chromedriver = './webdriver/chromedriver.exe'
else:
    sys.exit('Unsupported platform yet')

### Initialize
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = URL(path_config_file)

### Globals
# Get date ranges from config
config_file = ConfigParser()
config_file.read(path_config_file)
dep_date_min = Date(config_file.get('Dates', 'DepartureDate_Min'))
dep_date_max = Date(config_file.get('Dates', 'DepartureDate_Max'))
ret_date_min = Date(config_file.get('Dates', 'ReturnDate_Min'))
ret_date_max = Date(config_file.get('Dates', 'ReturnDate_Max'))
global results, everyReturnCombination, scrapedFlight
results = []
everyReturnCombination = []
scrapedFlight = Flight()

# 1
def forEachDepartureDate():
    global results, everyReturnCombination
    dep_date = Date(str(dep_date_min))
    while not dep_date.exceeds(dep_date_max):
        forEachReturnDate(dep_date)
        results.append(deepcopy(everyReturnCombination))
        pprint(everyReturnCombination)
        dep_date.incDay()

# 2
def forEachReturnDate(dep_date):
    global everyReturnCombination, scrapedFlight
    everyReturnCombination = []
    ret_date = Date(str(ret_date_min))
    while not ret_date.exceeds(ret_date_max):
        url.setDates(dep_date, ret_date)
        scrap(url.getFullUrl())
        scrapedFlight.departure = dep_date
        scrapedFlight.arrival =ret_date
        print scrapedFlight
        everyReturnCombination.append(deepcopy(scrapedFlight))
        ret_date.incDay()

# 3
def scrap(fixed_url):
    global scrapedFlight
    browser.get(fixed_url)

    # Wait for the search to be finished (100s)
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-completed'))
    )

    element = browser.find_element_by_xpath('//*[@id="flight-tickets-sortbar-cheapest"]/div/span[2]/span[1]')
    scrapedFlight.cheapest_price = int(element.text)
    element = browser.find_element_by_xpath('//*[@id="flight-tickets-sortbar-cheapest"]/div/span[3]')
    scrapedFlight.cheapest_duration = Time(element.text)
    element = browser.find_element_by_xpath('//*[@id="uiBestDealTab"]/span[2]/span[1]')
    scrapedFlight.bestdeal_price = int(element.text)
    element = browser.find_element_by_xpath('//*[@id="uiBestDealTab"]/span[3]')
    scrapedFlight.bestdeal_duration = Time(element.text)

# 3.1
def isSearchFinished():
    try:
        searchStatus = browser.find_element_by_xpath('//*[@id="searchProgressText"]')
        if 'Recherche termin' in searchStatus.text:
            return True
        else:
            return False
    except:
        return False

# 0
if "__main__" == __name__:
    start = datetime.now()

    forEachDepartureDate()
<<<<<<< HEAD
=======
    print 'Done.'
    #TODO: Add elapsed time
>>>>>>> master
    pprint(results)

    end = datetime.now()

    time_elapsed = end - start
    seconds = int(time_elapsed.total_seconds())
    hours = int(seconds / 3600)
    seconds = seconds - hours*3600
    minutes = int(seconds / 60)
    seconds = seconds - minutes*60
    print "\nFinished in %dh %dm %ds\n" % (hours, minutes, seconds)

    quit()

#TODO: Make the scrapping part a thread to process multiple date at same time (might need multiple webdriver instances)
