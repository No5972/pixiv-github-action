#导入VcrClient配置文件
import vcr_sample_conf 

#导入VCR相关模块
from baidubce import exception
from baidubce.services import vcr
from baidubce.services.vcr.vcr_client import VcrClient

import os

vcr_client = VcrClient(vcr_sample_conf.config)
preset = ""

path = os.getcwd()
get_dir = os.listdir(path)
for i in get_dir:
	if i.endswith('.jpg') or i.endswith('.png'):
		source = "https://imageproxy.pimg.tw/resize?url=https://raw.githubusercontent.com/No5972/pixiv-github-action/runner/" + i
		response = vcr_client.put_image(source, preset)
		if response.label == 'REJECT': 
			os.remove(i)
