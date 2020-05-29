# -- coding: utf-8 --

import platform
import socket

class cplatform:
    def __init__(self):
        pass

    def getplatform(self):
        dict_platform = {}
        dict_platform["computerName"] = computername = socket.gethostname()#socket.getfqdn(socket.gethostname())
        dict_platform["IP"] = socket.gethostbyname(computername)

        dict_platform["platform"] = platform.platform()
        dict_platform["version"] = platform.version()
        temp = platform.architecture()
        dict_platform["architecture"] = temp[0]+"_"+temp[1]
        dict_platform["machine"] = platform.machine()
        #dict_platform["node"] = platform.node()
        dict_platform["processor"] = platform.processor()

        return dict_platform

        '''
        import os
        os.getenv('COMPUTERNAME')

        import psutil  
        #获取网卡名称和其ip地址，不包括回环  
        def get_netcard():  
            netcard_info = []  
            info = psutil.net_if_addrs()  
            for k,v in info.items():  
                for item in v:  
                    if item[0] == 2 and not item[1]=='127.0.0.1':  
                        netcard_info.append((k,item[1]))  
            return netcard_info  
        '''

if __name__ == "__main__":
    cplatform().getplatform()