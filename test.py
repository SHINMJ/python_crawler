from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs, element
import time 
import pandas as pd

# https://map.naver.com/v5/search/경기%20시흥%20왁싱?
query = quote_plus('경기 시흥 왁싱')
url = f'http://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={query}'

chromedriver = './driver/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')        # headless chrome
options.add_argument('disable-gpu')    # GPU 사용 안함
options.add_argument('lang=ko_KR')    # 언어 설정

driver = webdriver.Chrome(chromedriver, options=options)

driver.get(url)

datalist = []

driver.implicitly_wait(5)

#loc-main-section-root > section > div > div:nth-child(2) > ul
#loc-main-section-root > section > div > div:nth-child(2) > ul > li:nth-child(1)

while True:
    time.sleep(3)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        time.sleep(2)

        new_height = driver.execute_script('return document.body.scrollHeight')

        if(new_height == last_height):
            time.sleep(2)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if(new_height == last_height):
                break
        
        last_height = new_height


    js_script = "document.querySelector(\"#place-app-root\").innerHTML"
    raw = driver.execute_script("return " + js_script)

    html = bs(raw, "html.parser")

    lis = html.select('#loc-main-section-root > section > div > div:nth-child(2) > ul > li')
    

    for li in lis:
        el = li.find('a', id='_.share')
        addr = el.attrs['data-line-description']
        name =  el.attrs['data-line-title']
        divs = li.div.next_sibling.findChildren('div')
        phone = divs[2].get_text()
        print(name + ' - ' + phone + ' - ' + addr )

    print(driver.find_element_by_css_selector('a.spnew_bf.cmm_pg_next.on'))

    try: driver.find_element_by_css_selector('a.spnew_bf.cmm_pg_next.on').click()
    except:
        print('done!!!!!')
        break
    finally:
        driver.quit()
    

# print(datalist)