import requests
import json
class RequestUtil:
    #类变量：通过类名访问
    session=requests.session()
    def send_request(self,method,url,data,headers,**kwargs):
        method=str(method).lower()
        rep=None
        if method=='get':
            rep = RequestUtil.session.request(method,url=url,params=data,headers=headers,**kwargs)
        else:
            data=json.dumps(data)
            rep = RequestUtil.session.request(method, url=url, data=data,headers=headers, **kwargs)
        return rep.text