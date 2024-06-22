from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_daily_newsint():
    today = []
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    news_url = 'https://www.thehindu.com/news/international/' 

    driver.get(news_url)

    headlines = driver.find_elements(By.XPATH, '/html/body/section[5]/div/div[2]') 

    # Extract and print the headlines
    for headline in headlines:
        
        data= headline.text.split('\n')
        for st in data:
            if len(st)> 35:
                 today.append(st)
              
    with open("intdailynews.txt", "w") as filenews:
                        for item in today:
                            filenews.write(item+"\n")
    # Close the browser
    
    
    driver.quit()

# get_daily_newsint()
