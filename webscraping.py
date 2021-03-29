import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://philembassyriyadh.timetap.com/emb/6473?schedulerLinkId=193383&locale=en-US&refId=r8607dc8373d7419aab61ce468eae088c#SERVICE'
URL_UAE = 'https://auhpe.checkappointments.com/emb/17358?schedulerLinkId=190513&locale=en-US&refId=rf66bdf80b931444ca2cec5a6bba8a157#SERVICE'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='gwt-HTML')
#print(results)

path = r'/Users/anonymous/Documents/Python/chromedriver'
browser = webdriver.Chrome(executable_path = path)
browser.get(URL)
browser.implicitly_wait(5)
#body > div:nth-child(12) > div:nth-child(2) > div > div:nth-child(4) > div > div > div > div > table
sel = browser.find_element_by_class_name('listStyle')
print("Test: " + sel.text)
browser.quit()
