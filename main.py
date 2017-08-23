"""#############################################################################
#                                                                              #
#   Momondo Scraper for best flight fare / travel time                         #
#                                                                              #
#   Description : 1. Get the user preferences for the date ranges              #
#                 2. Build search url with preferences and updated dates       #
#                 3. Launch Chrome to get the URL, wait for the search         #
#                    to be over, get the highlighted price and travel duration #
#                 4. Repeat for another departure date/return date combination #
#                 5. Plot the results                                          #
#   Author :      Nathan Bleuzen (with help of Thiago Marzagao's notes)        #
#   Written in :  Python 2.7                                                   #
#                                                                              #
#############################################################################"""

### Libraries
import platform, sys

### Custom modules
from controller import Controller

### Parameters
path_config_file = './search.conf'
path_to_webdriver_dir = './webdriver/' # ends with /
name_of_webdriver = 'chromedriver' # chromedriver OR phantomjs

path_to_webdriver = ''
if platform.system() == 'Darwin':
    path_to_webdriver = path_to_webdriver_dir + name_of_webdriver
elif platform.system() == 'Windows':
    path_to_webdriver = path_to_webdriver + name_of_webdriver + '.exe'
else:
    sys.exit('Unsupported platform yet')

if "__main__" == __name__:
    momondo_scraper = Controller(path_config_file, path_to_webdriver)
    momondo_scraper.main()
    quit()
