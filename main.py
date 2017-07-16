### Libraries
import platform, sys

### Custom modules
from scraper import Scraper

### Parameters
path_config_file = './search.conf'
if platform.system() == 'Darwin':
    path_to_chromedriver = './webdriver/chromedriver'
elif platform.system() == 'Windows':
    path_to_chromedriver = './webdriver/chromedriver.exe'
else:
    sys.exit('Unsupported platform yet')

if "__main__" == __name__:
    momondo_scraper = Scraper(path_config_file, path_to_chromedriver)
    momondo_scraper.main()
    quit()
