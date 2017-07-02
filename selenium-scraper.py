from selenium import webdriver
import time

# Get parameter from config file
children = ''


# Initialize
TripType = '&TripType='
SegNo = '&SegNo='
SO0 = '&SO0='
SD0 = '&SD0='
SDP0 = '&SDP0='
SO1 = '&SO1='
SD1 = '&SD1='
SDP1 = '&SDP1='
AD = '&AD='
CA = '&CA='
TK = '&TK='
DO = '&DO='
NA = '&NA='

# Get as conf
TripType += '2'
SegNo += '2'
SO0 += 'PAR'
SD0 += 'TPE'
SDP0 += '03-09-2017'
SO1 += 'TPE'
SD1 += 'PAR'
SDP1 += '23-02-2018'
AD += '1'
if children == '':
    CA = ''
else:
    CA += ''
TK += 'ECO'
DO += 'false'
NA += 'false'

url = 'https://www.momondo.fr/flightsearch?Search=true'
url += TripType + SegNo + SO0 + SD0 + SDP0 + SO1 + SD1 + SDP1 + AD + CA + TK + DO + NA

print url

path_to_chromedriver = '/Users/Nathan/Nextcloud/Git_Dev/momondo-scraper/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
#url = 'https://www.momondo.fr/flightsearch?Search=true'
#url += &TripType=2&SegNo=2&SO0=PAR&SD0=TPE&SDP0=03-09-2017&SO1=TPE&SD1=PAR&SDP1=23-02-2018&AD=1&TK=ECO&DO=false&NA=false'
#url = 'https://www.momondo.fr/flightsearch?Search=true&TripType=2&SegNo=2&SO0=PAR&SD0=TPE&SDP0=03-09-2017&SO1=TPE&SD1=PAR&SDP1=23-02-2018&AD=1&TK=ECO&DO=false&NA=false'


browser.get(url)

while True:
    try:
        searchStatus = browser.find_element_by_xpath('//*[@id="searchProgressText"]')
        if 'Recherche termin' in searchStatus:
            break
    except:
        print 'page not load yet'
        time.sleep(1)
        pass


price_cheapest = browser.find_element_by_xpath('//*[@id="flight-tickets-sortbar-cheapest"]/div/span[2]/span[1]')
print price_cheapest.text

#browser.switch_to_frame('mainFrame')
#browser.find_element_by_id('terms')
#browser.find_element_by_id('terms').clear()
#browser.find_element_by_id('terms').send_keys('balloon')
#browser.find_element_by_xpath('//*[@id="dateSelector1"]')
#browser.find_element_by_xpath('//*[@id="dateSelector1"]/option[contains(text(), "Today")]').click()
