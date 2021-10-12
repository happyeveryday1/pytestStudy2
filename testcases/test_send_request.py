import requests
import pytest
import re
import json

from common.yaml_util import YamlUtil
from common.requests_util import RequestUtil


class TestSendRequest:
    #类变量：通过类名访问
    session=requests.session()
    def setup(self):
        print("在每个用例执行前执行")

    def teardown(self):
        print("在每个用例执行后执行一次")

    def test_start(self,conn_database):
        url='http://47.107.116.139/phpwind/'

        # rep=RequestUtil().send_request("get",url)
        # print(rep.join())
        rep=TestSendRequest.session.request("get",url=url)

        #通过正则表达式获取鉴权码
        YamlUtil().write_extract_yaml({'csrf_token': re.search('name="csrf_token" value="(.*?)"',rep.text)[1]})
        # TestSendRequest.csrf_token=re.search('name="csrf_token" value="(.*?)"',rep.text)[1]
        # print(TestSendRequest.csrf_token)

    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_login.yml'))
    def test_login(self,caseinfo):
        csrf_token=YamlUtil().read_extract_yaml('csrf_token')
        method=caseinfo['request']['method']
        url=caseinfo['request']['url']
        headers=caseinfo['request']['headers']
        data=caseinfo['request']['data']
        data['csrf_token']=csrf_token

        result=RequestUtil().send_request(method,url,data,headers)
        print(result)
        # rep=TestSendRequest.session.request(method,url=url,data=data,headers=headers)
        # print(rep.json())



