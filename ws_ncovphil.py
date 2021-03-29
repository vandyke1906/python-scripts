import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://dohph.maps.arcgis.com/apps/opsdashboard/index.html#/3dda5e52a7244f12a4fb3d697e32fd39'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='gwt-HTML')
#print(results)

path = r'/Users/anonymous/Documents/Python/chromedriver'
browser = webdriver.Chrome(executable_path = path)
browser.get(URL)

#wait to load ajax page
browser.implicitly_wait(40)

#get list item confirmed
sel = browser.find_elements_by_class_name('feature-list-item')
for span in sel:
    print(span.text)


#get list total
##ember269 > svg > g.responsive-text-label > svg > text
##ember269 > svg > g.responsive-text-label
indicators = browser.find_elements_by_css_selector('svg.responsive-text-group')
for val_i in indicators:
    print('indicator:', val_i.text)

browser.quit()
