# -*- coding:utf-8 -*-  
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '10655150'
API_KEY = 'LhdqMzzyltNdvdz0naWEYTQ4'
SECRET_KEY = 'wSfsaGGQtsbAjGVK6DBDALVV3LISgZv9'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})

