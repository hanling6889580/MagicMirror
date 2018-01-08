# -*- coding: utf-8 -*-
import urllib2
import json
import sys
from aip import AipSpeech

reload(sys)
sys.setdefaultencoding('utf-8')


url='https://free-api.heweather.com/s6/weather/now?location=CN101010100&key=9cee7a70af1e479ea94cbcd9722d1870'
resp=urllib2.urlopen(url).read().decode('utf-8')
json_data = json.loads(resp)

data = json_data['HeWeather6'][0]



#获取城市
city = data['basic']['cid']

#获取现在的天气、温度、体感温度、风向、风力等级
now_weather = data['now']["cond_txt"]
now_tmp = data['now']['tmp']
now_fl = data['now']['fl']
now_wind_dir = data['now']["wind_dir"]
now_wind_sc = data['now']["wind_sc"]

weather_forcast_txt="%s今天天气%s,温度%s,体感温度%s,风向%s,风力等级%s"%(city,now_weather,now_tmp,now_fl,now_wind_dir,now_wind_sc)



#百度语音合成
APP_ID = '10289797'
API_KEY = 'giOywYhsdhFQ4npq5lqDXfK3'
SECRET_KEY = 'jv7KTB94EPiNROYPxb7LtaUKCE2oA1ug'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis(weather_forcast_txt, 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('E:/baidu-AI/auido222.mp3', 'wb') as f:
        f.write(result)
        
