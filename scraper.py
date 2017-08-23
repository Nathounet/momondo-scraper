### Libraries
from time import sleep
from Queue import Queue
from random import random
from selenium import webdriver
from threading import current_thread
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

### Custom modules
from url import URL
from shorttime import Time
from flight import Flight

class Scraper():
    def __init__(self, config_parameters, path_to_webdriver):
        self.url = URL(config_parameters)
        self.initWebdriver(path_to_webdriver)


    def initWebdriver(self, path_to_webdriver):
        if path_to_webdriver.endswith('phantomjs'):
            dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = (
                 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
            self.browser = webdriver.PhantomJS(executable_path = path_to_webdriver, desired_capabilities = dcap)
        else: #chromedriver
            self.browser = webdriver.Chrome(executable_path = path_to_webdriver)
        self.browser.set_window_size(400, 700)


    def processDateCombination(self, results_dep, results_lock, date_queue, exit_flag):
        # Wait between 0 and 17.3s before first search
        delay = (random() * 10) + (random() * 7.3)
        print '%s Sleeping for %5.2f seconds...' % (current_thread().name, delay)
        exit_flag.wait(timeout=delay)

        while not date_queue.empty():
            dep_date, ret_date = date_queue.get()

            scrapedFlight = self.scrap(dep_date, ret_date)
            print current_thread().name, scrapedFlight

            with results_lock:
                results_dep.append(scrapedFlight)
                print "Processed: %2d / Remaining: %2d" % (len(results_dep), date_queue.qsize())
            date_queue.task_done()

            if date_queue.empty():
                print "All date combinations processed, exiting threads"
                exit_flag.set()
            else:
                # Wait between 5 and 13.3s between each search to make it less boty
                delay = 5 + (random() * 5) + (random() * 1.3)
                print '%s Sleeping for %.2f seconds...' % (current_thread().name, delay)
                exit_flag.wait(timeout=delay)

        exit_flag.set()
        self.browser.quit()


    def scrap(self, dep_date, ret_date):
        self.url.setDates(dep_date.strftime('%d-%m-%Y'), ret_date.strftime('%d-%m-%Y'))
        scrapedFlight = self.loadPage(self.url.getFullUrl())
        scrapedFlight.date_departure = dep_date
        scrapedFlight.date_this_way = dep_date # here this way = departure
        scrapedFlight.date_return = ret_date
        scrapedFlight.date_other_way = ret_date
        return scrapedFlight


    def loadPage(self, fixed_url):
        scrapedFlight = Flight()
        self.browser.get(fixed_url)

        try:
            # Wait for the search to be finished (100s)
            element = WebDriverWait(self.browser, 100).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'search-completed')))
        except:
            self.browser.save_screenshot('out.png');
            self.browser.quit()
            assert 2==1

        element = self.browser.find_element_by_xpath('//*[@id="flight-tickets-sortbar-cheapest"]/div/span[2]/span[1]')
        scrapedFlight.cheapest_price = int(element.text)
        element = self.browser.find_element_by_xpath('//*[@id="flight-tickets-sortbar-cheapest"]/div/span[3]')
        scrapedFlight.cheapest_duration = Time(element.text)
        element = self.browser.find_element_by_xpath('//*[@id="uiBestDealTab"]/span[2]/span[1]')
        scrapedFlight.bestdeal_price = int(element.text)
        element = self.browser.find_element_by_xpath('//*[@id="uiBestDealTab"]/span[3]')
        scrapedFlight.bestdeal_duration = Time(element.text)
        return scrapedFlight
