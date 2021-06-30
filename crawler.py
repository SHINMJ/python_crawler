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

# https://map.naver.com/v5/search/경기%20시흥%20왁싱?
query = quote_plus('경기 안양 왁싱')
url = f'https://map.naver.com/v5/search/{query}'

chromedriver = './driver/chromedriver'
options = webdriver.ChromeOptions()
# options.add_argument('headless')        # headless chrome
# options.add_argument('disable-gpu')    # GPU 사용 안함
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

    # obj = driver.find_element_by_tag_name('html')
    # obj.send_keys(Keys.END)

    # last_height = driver.execute_script("return document.body.scrollHeight")

    # print(driver.execute_script('return document.body.className'))

    # while True:
    #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    #     time.sleep(2)

    #     new_height = driver.execute_script('return document.body.scrollHeight')
    #     print('new_height : ' + str(new_height) + ' , last_height : ' + str(last_height))
    #     if(new_height == last_height):
    #         time.sleep(2)
    #         new_height = driver.execute_script('return document.body.scrollHeight')
    #         if(new_height == last_height):
    #             break
        
    #     last_height = new_height


    js_script = "document.querySelector(\"#app-root\").innerHTML"
    raw = driver.execute_script("return " + js_script)

    html = bs(raw, "html.parser")

    lis = html.select('#_pcmap_list_scroll_container > ul > li')
    #_pcmap_list_scroll_container > ul > li:nth-child(45) > div._3ZU00._1rBq3 > a:nth-child(1)
    print(len(lis))
    for idx, li in enumerate(lis):
        el = li.find('span', '_3Apve')
        name = el.get_text()
        print(driver.find_element_by_xpath('//*[@id="_pcmap_list_scroll_container"]/ul/li['+str(idx+1)+']/div[2]/a[1]').text)
        driver.find_element_by_xpath('//*[@id="_pcmap_list_scroll_container"]/ul/li['+str(idx+1)+']/div[2]/a[1]').click()
       


        time.sleep(5)

        driver.switch_to.default_content()
        driver.switch_to.frame('entryIframe')

        try:
            elements = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".place_on_pcmap"))
            )
        except TimeoutException:
            print('timout!!!!!!')
        finally:
            driver.quit() 
        
        phone = driver.find_element_by_xpath('//*[@id="app-root"]/div/div[2]/div[4]/div/div[2]/div/ul/li[1]/div/span[1]')
        addr = driver.find_element_by_xpath('//*[@id="app-root"]/div/div[2]/div[4]/div/div[2]/div/ul/li[2]/div/span[1]')
        print(str(idx)+ '' + name + '  : ' + phone.text+'  : ' + addr.text)
        driver.switch_to.default_content()
        driver.switch_to.frame('searchIframe')

        # driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-close-button/button').click()
        time.sleep(1)


    try: driver.find_element_by_css_selector('a.spnew_bf.cmm_pg_next.on').click()
    except:
        print('done!!!!!')
        break
    finally:
        driver.switch_to.default_content()
        driver.quit()
    

# print(datalist)