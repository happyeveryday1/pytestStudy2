import requests
class RequestUtil:
    session=requests.session()
    def send_request(self,method,url,data, headers,**kwargs):
        rep=RequestUtil().session.request(method=method,url=url,data=data,headers=headers,**kwargs)
        return rep.text