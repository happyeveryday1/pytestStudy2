import requests
import pytest
import re
import json
class TestSendRequest:
    #类变量：通过类名访问
    access_token=''
    csrf_token=''
    cks=''


    # def test_file_opload(self):
    #     url=''
    #     data={
    #         'media':open(r"E:\shu.png","rb")
    #     }
    #     requests.post(url=url,files=data)
    def test_start(self):
        url='http://47.107.116.139/phpwind/'
        rep=requests.request("get",url=url)
        #网页只能通过文本格式打开
        #print(rep.text)
        #通过正则表达式获取鉴权码
        TestSendRequest.csrf_token=re.search('name="csrf_token" value="(.*?)"',rep.text)[1]
        print(TestSendRequest.csrf_token)
        TestSendRequest.cks=rep.cookies

    def test_login(self):
        url='http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
        headers={
            "Accept":"application/json,text/javascript,/;q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }
        data={
            "username":"msxy",
            "password":"msxy",
            "csrf_token":TestSendRequest.csrf_token,
            "backurl":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        rep=requests.request('post',url=url,data=data,headers=headers,cookies=TestSendRequest.cks)
        print(rep.json())
if __name__ == '__main__':
    pytest.main(['-vs'])

