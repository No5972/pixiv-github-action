#导入VcrClient配置文件
import vcr_sample_conf 

#导入VCR相关模块
from baidubce import exception
from baidubce.services import vcr
from baidubce.services.vcr.vcr_client import VcrClient

import os
from urllib import parse

vcr_client = VcrClient(vcr_sample_conf.config)
preset = ""

path = os.getcwd()
get_dir = os.listdir(path)
for i in get_dir:
	if i.endswith('.jpg') or i.endswith('.png'):
		source = "https://imageproxy.pimg.tw/resize?url=https://raw.githubusercontent.com/No5972/pixiv-github-action/runner/" + parse.quote(i)
		try:
			response = vcr_client.put_image(source, preset)
			if response.label == 'REJECT' or response.label == 'REVIEW': 
				for k in response.results:
					print(i + ' BAD - ' + k.type)
					if k.type != 'ad_marketing' and k.type != 'ad_brand':
						os.remove(i)
						break
			else:
				print(i + ' GOOD')
		except:
			print(i + ' BCE_ERROR')
			os.remove(i)
