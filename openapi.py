import requests
from urllib.parse import quote_plus
import pandas as pd
import time

CLIENT_ID='VsdLbvNh6_WkFOpn6mVY'
CLIENT_SECRET='egHtm8bPsa'
 
# 네이버 api call
def call(keyword, start):
    encText = quote_plus(keyword)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText + "&display=5" + "&start=" + str(start)

    result = requests.get(url=url, headers={"X-Naver-Client-Id":CLIENT_ID,
                                          "X-Naver-Client-Secret":CLIENT_SECRET})
    print(result.json())  # Response [200]
    return result.json()
 
# 1000개의 검색 결과 받아오기
def get1000results(keyword):
    list = []
    for num in range(0,20):
        list = list + call(keyword, num * 5 + 1)['items'] # list 안에 키값이 ’item’인 애들만 넣기
        time.sleep(10)
    return list


datalist = get1000results("경기 안양 왁싱")

for data in datalist:
    print(data['title'])

# write_wb = Workbook()
 
# #이름이 있는 시트를 생성
# write_ws = write_wb.create_sheet('경기안양')
 
# #Sheet1에다 입력
# write_ws = write_wb.active
# write_ws['A1'] = '숫자'
 
# #행 단위로 추가
# write_ws.append([1,2,3])
 
# #셀 단위로 추가
# write_ws.cell(5,5,'5행5열')
# write_wb.save('./search.xlsx')