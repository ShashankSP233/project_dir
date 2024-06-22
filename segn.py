from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import time

def get_site(srch):
    today = []
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    hisfile  = open("history.txt", "a+")
    hisfile.write(srch+'\t' + str(datetime.datetime.now()) + "\n")
    srchurl = 'https://www.google.com/search?q='+srch
    print(srchurl)
    driver.get(srchurl)
    time.sleep(40)

get_site('java')

