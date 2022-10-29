from bs4 import BeautifulSoup as bs
from urllib.parse import urlencode, unquote
import requests
from datetime import datetime
from datetime import time

today = datetime.now()
apiday = repr(today.year) + repr(today.month) + repr(today.day)
apitime = "0"
if today.hour < 10:
    apitime = apitime + repr(today.hour)
else:
    apitime = repr(today.hour)

if today.minute < 10:
    apitime = apitime + "0" + repr(today.minute)
else:
    apitime = apitime + repr(today.minute)

weather_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
land = {'seoul' : [60, 127], 'busan' : [97, 74], 'daegu' : [89, 90], 'incheon' : [55, 124], 'gwangju' : [60, 74], 'daejeon' : [68, 100], 'ulsan' : [101, 84], 'sejong' : [66, 103], 'gyeonggi' : [60, 120], 'gangwon' : [92, 131], 'chungbuk' : [69, 106], 'chungnam' : [55, 101], 'jeonbuk' : [63, 88], 'jeonnam' : [71, 68], 'gyeongbuk' : [100, 95], 'gyeongnam' : [96, 77], 'jeju' : [60, 38]}


landxy = land[input("Input your field: ")]
weather_params = {
    'serviceKey' : 'px1UZk9vqM/E0+ZyvLdQRypMD+MYp03T6knwyur6dZTJXOvQwKmgiIP3E72GUv7prZtzU6U/9aIceThfLHW3CQ==',
    'base_date' : apiday,
    'base_time' : "0600",
    'nx' : landxy[0],
    'ny' : landxy[1],
    'numOfRows' : '1000',
    'pageNo' : '1',
    'dataType' : 'JSON'
}
weather_request_url = weather_url + '?' + urlencode(weather_params)

weather_response = requests.get(weather_request_url)
print(weather_response.text)
print(apitime)
mushroom_soup = bs(weather_response.content, 'html.parser')
weather_report = mushroom_soup.find('obsrValue')
print()

