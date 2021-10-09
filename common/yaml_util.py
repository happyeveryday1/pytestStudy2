import os
import yaml

class YamlUtil:
    #读取extract.yaml
    def read_extract_yaml(self,key):
        with open(os.getcwd()+'/extract.yml',mode='r',encoding='utf-8') as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key];

    # 写入extract.yaml
    def write_extract_yaml(self,data):
        with open(os.getcwd() + '/extract.yml', mode='a', encoding='utf-8') as f:
            yaml.dump(data=data,stream=f, allow_unicode=True)

    # 清除extract.yaml
    def clear_extract_yaml(self):
        with open(os.getcwd() + '/extract.yml', mode='w', encoding='utf-8') as f:
            f.truncate()

