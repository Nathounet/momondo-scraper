### Libraries
from time import sleep
from copy import deepcopy
from pprint import pprint
from random import random
from datetime import datetime, timedelta, time
from selenium import webdriver
from ConfigParser import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Custom modules
from flight import Flight
from url import URL


class Scraper():
    def __init__(self, path_config_file, path_to_chromedriver):
        self.getConfig(path_config_file)
        self.url = URL(path_config_file)

        self.browser = webdriver.Chrome(executable_path = path_to_chromedriver)
        self.results = []
        self.everyReturnCombination = []
        self.scrapedFlight = Flight()


    def getConfig(self, path_config_file):
        # Get date ranges from config
        config_file = ConfigParser()
        config_file.read(path_config_file)
        self.dep_date_min = datetime.strptime(config_file.get('Dates', 'DepartureDate_Min'), '%d-%m-%Y')
        self.dep_date_max = datetime.strptime(config_file.get('Dates', 'DepartureDate_Max'), '%d-%m-%Y')
        self.ret_date_min = datetime.strptime(config_file.get('Dates', 'ReturnDate_Min'), '%d-%m-%Y')
        self.ret_date_max = datetime.strptime(config_file.get('Dates', 'ReturnDate_Max'), '%d-%m-%Y')


    def main(self):
        start = datetime.now()

        self.forEachDepartureDate()
        print '\n######## RESULTS ########'
        pprint(self.results)

        end = datetime.now()

        time_elapsed = end - start
        seconds = int(time_elapsed.total_seconds())
        hours = int(seconds / 3600)
        seconds = seconds - hours*3600
        minutes = int(seconds / 60)
        seconds = seconds - minutes*60
        print "\nFinished in %dh %dm %ds\n" % (hours, minutes, seconds)

    # 1
    def forEachDepartureDate(self):
        dep_date = deepcopy(self.dep_date_min)
        while not dep_date > self.dep_date_max:
            self.forEachReturnDate(dep_date)
            self.results.append(deepcopy(self.everyReturnCombination))
            pprint(self.everyReturnCombination)
            dep_date += timedelta(days=1)

    # 2
    def forEachReturnDate(self, dep_date):
        self.everyReturnCombination = []
        ret_date = deepcopy(self.ret_date_min)
        while not ret_date > self.ret_date_max:
            self.url.setDates(dep_date.strftime('%d-%m-%Y'), ret_date.strftime('%d-%m-%Y'))
            self.scrap(self.url.getFullUrl())
            self.scrapedFlight.departure_date = dep_date
            self.scrapedFlight.return_date = ret_date
            print self.scrapedFlight
            self.everyReturnCombination.append(deepcopy(self.scrapedFlight))
            ret_date += timedelta(days=1)
            # Wait between 5 and 9.7s between each search to make it less boty
            seconds = 5 + (random() * 4) + (random() * 0.7)
            print 'Sleeping for %.2f seconds...' % (seconds)
            sleep(seconds)

    # 3
    def scrap(self, fixed_url):
        self.browser.get(fixed_url)

        # Wait for the search to be finished (100s)
        element = WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-completed')))

        element = self.browser.find_element_by_xpath('//*[@id="flight-tickets-sortbar-cheapest"]/div/span[2]/span[1]')
        self.scrapedFlight.cheapest_price = int(element.text)
        element = self.browser.find_element_by_xpath('//*[@id="flight-tickets-sortbar-cheapest"]/div/span[3]')
        self.scrapedFlight.cheapest_duration = datetime.strptime(element.text, '%Hh%Mm (Moyenne)')
        element = self.browser.find_element_by_xpath('//*[@id="uiBestDealTab"]/span[2]/span[1]')
        self.scrapedFlight.bestdeal_price = int(element.text)
        element = self.browser.find_element_by_xpath('//*[@id="uiBestDealTab"]/span[3]')
        self.scrapedFlight.bestdeal_duration = datetime.strptime(element.text, '%Hh%Mm (Moyenne)')


#TODO+ Find lowest price in Cheapest and lowest duration in BestDeal for every departure date and every return date
#       Create a list for each (4 lists: cheapest_departure, shortest_departure, cheapest_return, shortest_return)
#       Plot cheapest and shortest on same graph showing both price and duration for cheapest_ and shortest_
#TODO- Make the scrapping part a thread to process multiple date at same time (might need multiple webdriver instances)
