from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_daily_news():
    today = []
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    news_url = 'https://www.thehindu.com/news/national/' 

    driver.get(news_url)

    headlines = driver.find_elements(By.XPATH, '/html/body/section[4]') 

    # Extract and print the headlines
    for headline in headlines:
        
        data= headline.text.split('\n')
        for st in data:
            if len(st)> 25:
                 today.append(st)
              
    with open("dailynews.txt", "w", encoding="utf-8") as filenews:
                        for item in today:
                            filenews.write(item+"\n")
    # Close the browser
    
    
    driver.quit()

# get_daily_news()
