from selenium import webdriver

path_to_chromedriver = '/Users/Nathan/Nextcloud/Git_Dev/momondo-scraper/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://www.momondo.fr/flightsearch?Search=true&TripType=2&SegNo=2&SO0=PAR&SD0=TPE&SDP0=03-09-2017&SO1=TPE&SD1=PAR&SDP1=23-02-2018&AD=1&TK=ECO&DO=false&NA=false'
browser.get(url)
#browser.switch_to_frame('mainFrame')
#browser.find_element_by_id('terms')
#browser.find_element_by_id('terms').clear()
#browser.find_element_by_id('terms').send_keys('balloon')
#browser.find_element_by_xpath('//*[@id="dateSelector1"]')
#browser.find_element_by_xpath('//*[@id="dateSelector1"]/option[contains(text(), "Today")]').click()
