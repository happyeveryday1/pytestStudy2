import requests
import pytest
import re
import json

from common.yaml_util import YamlUtil
from common.requests_util import RequestUtil


class TestSendRequest:
    def test_start(self,conn_database):
        url='http://47.107.116.139/phpwind/'
        method='get'
        data={}
        headers={}
        rep=RequestUtil().send_request(method,url,data,headers)

        #通过正则表达式获取鉴权码
        YamlUtil().write_extract_yaml({'csrf_token': re.search('name="csrf_token" value="(.*?)"',rep)[1]})
        #YamlUtil().write_extract_yaml({'csrf_token': re.search('name="csrf_token" value="(.*?)"', rep.text)[1]})

    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_login.yml'))
    def test_login(self,caseinfo):
        csrf_token=YamlUtil().read_extract_yaml('csrf_token')
        method=caseinfo['request']['method']
        url=caseinfo['request']['url']
        data=caseinfo['request']['data']
        data['csrf_token']=csrf_token
        headers = caseinfo['request']['headers']
        result=RequestUtil().send_request(method, url, data,headers)
        print(json.loads(result))

        # rep=TestSendRequest.session.request(method,url=url,data=data,headers=headers)
        # print(rep.json())



