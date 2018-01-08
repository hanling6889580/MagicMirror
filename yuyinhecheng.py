# -*- coding: utf-8 -*-

from aip import AipSpeech
APP_ID ='10289797'
API_KEY ='giOywYhsdhFQ4npq5lqDXfK3'
SECRET_KEY ='jv7KTB94EPiNROYPxb7LtaUKCE2oA1ug'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
client.asr(get_file_content('E:\\baidu-AI\yuyinshibie\public\\8k.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})
#语音合成
result  = client.synthesis('为什么称为喜剧，其中有一个男主角最后是在魔力的作用下才与爱慕他的女主角的长相厮守', 'zh', 1, {
    'vol': 5,
})
if not isinstance(result, dict):
    with open('E:\\baidu-AI\\auido.mp3', 'wb') as f:
        f.write(result)
