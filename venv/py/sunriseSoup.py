import time
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users\minyou\PycharmProjects\BeautifulSalad/venv\webdriver\chromedriver')

driver.get("http://runway.vogue.co.kr/2018/02/21/ready-to-wear-2018-fw-gucci/#0")
time.sleep(1)

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 1

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -=1

provider_elems = driver.find_elements_by_tag_name("img")
num = 1
for post in provider_elems:
    name = "image"+str(num)+".jpg"
    urllib.request.urlretrieve(post.get_attribute("src"),name)
    print(post.get_attribute("src"))
    num += 1
