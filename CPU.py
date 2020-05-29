# -- coding: utf-8 --

import psutil

class cCPU:
    def __init__(self):
        pass

    def get_cpu_info(self,computer_ID):
        num = psutil.cpu_count()  # 返回系统CPU
        lnum = psutil.cpu_count(logical=True)   #返回系统逻辑CPU
        cpu_times = psutil.cpu_times(percpu=True)
        '''
        a= psutil.cpu_percent() #返回CPU利用率
        b=psutil.cpu_times_percent(interval=None, percpu=False)
        c=psutil.cpu_count(logical=True)   #返回系统逻辑CPU
        d=psutil.cpu_stats()              #返回CPU的统计信息
        e=psutil.cpu_freq(percpu=False)   #返回CPU的频率
        '''

        return [{"computer_ID":computer_ID,"cpu_count":num,"cpu_logical_count":lnum,"user":y.user,"`system`":y.system,"idle":y.idle,"interrupt":y.interrupt,"dpc":y.dpc} for y in cpu_times]

if __name__ == "__main__":
    cCPU().get_cpu_info(5)