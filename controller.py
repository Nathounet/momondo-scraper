### Libraries
import threading
from time import sleep
from Queue import Queue
from copy import deepcopy
from pprint import pprint
from random import random
from itertools import groupby
from operator import attrgetter
from datetime import datetime, timedelta

### Custom modules
from plot import Plot
from config import Config
from scraper import Scraper
from csvwriter import CsvWriter
from autotest import AutoTest

#TODO: handle no result, block page, 403 forbidden error with empty Flight that will not be used in the final results

class Controller():
    def __init__(self, path_config_file, path_to_webdriver):
        self.results_dep = []
        self.results_ret = []
        self.config_parameters = Config(path_config_file)
        self.path_to_webdriver = path_to_webdriver


    def main(self):
        start = datetime.now()
        print "Searching for flights from %s to %s" % (self.config_parameters.departure, self.config_parameters.arrival)

        self.createDateDivision()
        self.createThreads()
        #AutoTest(self.results_dep) # create results for test purpose

        self.sortResults()
        self.printResults()

        CsvWriter(self.config_parameters, self.results_dep, self.results_ret)
        Plot(self.config_parameters, self.results_dep, self.results_ret)

        end = datetime.now()

        time_elapsed = end - start
        seconds = int(time_elapsed.total_seconds())
        hours = int(seconds / 3600)
        seconds = seconds - hours*3600
        minutes = int(seconds / 60)
        seconds = seconds - minutes*60
        print "\nFinished in %dh %dm %ds\n" % (hours, minutes, seconds)


    def createDateDivision(self):
        self.date_queue = Queue(maxsize=0)
        dep_date = deepcopy(self.config_parameters.dep_date_min)
        while not dep_date > self.config_parameters.dep_date_max:
            ret_date = deepcopy(self.config_parameters.ret_date_min)
            while not ret_date > self.config_parameters.ret_date_max:
                self.date_queue.put((dep_date, ret_date))
                ret_date += timedelta(days=1)
            dep_date += timedelta(days=1)
        print "%d date combinations (Departure/Return) will have to be searched for." % (self.date_queue.qsize())


    def createThreads(self):
        results_lock = threading.Lock()
        exit_flag = threading.Event()
        print "Starting the %d automated browsers" % (num_thread)
        for num_thread in range(self.config_parameters.max_threads):
            scraper = Scraper(self.config_parameters, self.path_to_webdriver)
            worker = threading.Thread(target=scraper.processDateCombination,
                                name="[#"+str(num_thread)+"]",
                                args=(self.results_dep, results_lock, self.date_queue, exit_flag))
            worker.setDaemon(False)
            worker.start()
        self.date_queue.join()
        print "All date combinations processed or in-process, waiting for threads to exit"

        main_thread = threading.currentThread()
        for worker in threading.enumerate():
            if worker is main_thread:
                continue
            worker.join()
        print "All threads ended"


    def sortResults(self):
        # Sort results_dep, create and sort results_ret
        self.results_dep.sort(key=attrgetter('date_departure'))
        self.results_ret = deepcopy(sorted(self.results_dep, key=attrgetter('date_return')))
        self.results_dep = [list(grp) for _, grp in groupby(self.results_dep, attrgetter('date_departure'))]
        self.results_ret = [list(grp) for _, grp in groupby(self.results_ret, attrgetter('date_return'))]
        # Dates this_way and other_way must be inverted for results_ret
        for nb_ret, list_departure_flight in enumerate(self.results_ret):
            for nb_dep, departure_flight in enumerate(list_departure_flight):
                self.results_ret[nb_ret][nb_dep].date_this_way = self.results_ret[nb_ret][nb_dep].date_return
                self.results_ret[nb_ret][nb_dep].date_other_way = self.results_ret[nb_ret][nb_dep].date_departure


    def printResults(self):
        print '\n######## RESULTS ########'
        print '--- DEPARTURES ---'
        pprint(self.results_dep)
        print '\n--- RETURNS ---'
        pprint(self.results_ret)
