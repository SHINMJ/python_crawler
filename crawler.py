from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs, element
import time 
import pandas as pd

def readdata(driver, lis, index) :
    print(len(lis))
    for idx, li in enumerate(lis):
        el = li.find('span', '_3Apve')
        name = el.get_text()
        
        aele = ''
        try:
            aele = driver.find_element_by_css_selector('#_pcmap_list_scroll_container > ul > li:nth-child('+str(index+idx+1)+') > div:nth-child(2) > a:nth-child(1)') 
        except:
            aele = driver.find_element_by_css_selector('#_pcmap_list_scroll_container > ul > li:nth-child('+str(index+idx+1)+') > div:nth-child(1) > a:nth-child(1)')

        print(name)
        aele.click()
       
        time.sleep(5)

        # driver.switch_to.default_content()
        # driver.switch_to.frame('entryIframe')

        # # print(driver.page_source)
        # subhtml = bs(driver.page_source, 'html.parser')
        # span = subhtml.select('div.place_section_content > ul > li > div > span')
        # phone = span[0].get_text()
        # addr = span[2].get_text()
        # print(str(idx)+ ' ' + name + '  : ' + phone+'  : ' + addr)
        # driver.switch_to.default_content()
        # driver.switch_to.frame('searchIframe')
        # # print(driver.page_source)
        # # driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-close-button/button').click()
        # time.sleep(1)


# https://map.naver.com/v5/search/경기%20시흥%20왁싱?
query = quote_plus('경기 안양 왁싱')
url = f'https://map.naver.com/v5/search/{query}'

chromedriver = './chromedriver'
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
    driver.switch_to.default_content()
    driver.switch_to.frame("searchIframe")


    time.sleep(1)

    #_pcmap_list_scroll_container > ul > li:nth-child(45) > div._3ZU00._1rBq3 > a:nth-child(1)
    for i in range(0, 5):
        js_script = "document.querySelector(\"#app-root\").innerHTML"
        raw = driver.execute_script("return " + js_script)

        html = bs(raw, "html.parser")

        lis = html.select('#_pcmap_list_scroll_container > ul > li')
        readlis = lis[(10*i):]
        print(str(len(lis))+" : "+str(i) + " : " + str(len(readlis)))
        readdata(driver=driver, lis=readlis, index=(10*i))

    try: 
        driver.find_element_by_css_selector('div._2ky45 > a:last-child').click()
        time.sleep(5)
    except:
        print('done!!!!!')
        break
    finally:
        driver.switch_to.default_content()
        driver.quit()
    

# print(datalist)