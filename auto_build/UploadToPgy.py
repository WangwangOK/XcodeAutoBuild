#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#*******************************************************************
#**************************👆头部代码解释*****************************
#第一行：告诉Linux/OS X系统，这是python可执行程序
#第二行：告诉python解释器，按照utf-8的编码读取源代码，否则会出现乱码
#*******************************************************************

#由于python源代码也是一个文本文件，所以，当你源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为utf-8编码。
#当python读取源代码的时候，为了让它按utf-8编码读取。我们通常在文件开头写上上面两行代码
from optparse import OptionParser
import subprocess
import requests

PGYER_UPLOAD_URL  = "http://www.pgyer.com/apiv1/app/upload"
DOWNLOAD_BASE_URL = "http://www.pgyer.com"
USER_KEY          = "eac08a60086cef4ac700321e47387117"
API_KEY           = "cc124ba28de1f55c2e162501493e5898"

IPA_PATH		  = "BBK_iOS.ipa"
PGY_APP_PASSWORD  = "123456"

def parserUploadResult(jsonResult):
	resultCode = jsonResult['code']
	if resultCode == 0:
		downUrl = DOWNLOAD_BASE_URL +"/"+jsonResult['data']['appShortcutUrl']
		print "Upload Success"
		print "DownUrl is:" + downUrl
	else:
		print "Upload Fail!"
		print "Reason:"+jsonResult['message']

def uploadIpaToPgyer(ipaPath):
    print "ipaPath:"+ipaPath
    #open函数
    #@param 第一个参数:当前要操作的这个文件的地址
    #@param 第二个参数:对当前这个文件的操作，'r'读模式、'w'写模式、'a'追加模式、'b'二进制模式、'+'读/写模式。
    #例如：
	# rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
	# w     以写方式打开，
	# a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
	# r+     以读写模式打开
	# w+     以读写模式打开 (参见 w )
	# a+     以读写模式打开 (参见 a )
	# rb     以二进制读模式打开
	# wb     以二进制写模式打开 (参见 w )
	# ab     以二进制追加模式打开 (参见 a )
	# rb+    以二进制读写模式打开 (参见 r+ )
	# wb+    以二进制读写模式打开 (参见 w+ )
	# ab+    以二进制读写模式打开 (参见 a+ )
	# a.     Python 2.3 中新增
    files = {'file': open(ipaPath, 'rb')}
    headers = {'enctype':'multipart/form-data'}
    payload = {'uKey':USER_KEY,'_api_key':API_KEY,'publishRange':'2','isPublishToPublic':'2', 'password':PGY_APP_PASSWORD}
    print "uploading...."
    r = requests.post(PGYER_UPLOAD_URL, data = payload ,files=files,headers=headers)
    if r.status_code == requests.codes.ok:
    	print r.status_code
        result = r.json()
        parserUploadResult(result)
    else:
        print 'HTTPError,Code:'+r.status_code

def main():
	print '\n'
	print '请设置App安装密码(默认密码为:123456)'
	print '\n'
	PGY_APP_PASSWORD = raw_input()
	uploadIpaToPgyer(IPA_PATH)

if __name__ == '__main__':
	main()