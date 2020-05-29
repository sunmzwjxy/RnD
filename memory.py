# -- coding: utf-8 --

import psutil

class cmemory:
    def __init__(self):
        pass
    
    def get_mem_info(self,computer_ID):
        dict_mem = {}
        mem_info = psutil.virtual_memory()
        swapmem_info = psutil.swap_memory()

        #svmem(total=8481992704L, available=2137763840L, percent=74.8, used=6344228864L, free=2137763840L)
        #sswap(total=16962064384L, used=6649405440L, free=10312658944L, percent=39.2, sin=0, sout=0)
        dict_mem["computer_ID"] = computer_ID
        dict_mem["total"] = mem_info.total
        dict_mem["available"] = mem_info.available
        dict_mem["percent"] = mem_info.percent
        dict_mem["used"] = mem_info.used
        dict_mem["free"] = mem_info.free

        dict_mem["swap_total"] = swapmem_info.total
        dict_mem["swap_used"] = swapmem_info.used
        dict_mem["swap_free"] = swapmem_info.free
        dict_mem["swap_percent"] = swapmem_info.percent
        dict_mem["swap_sin"] = swapmem_info.sin
        dict_mem["swap_sout"] = swapmem_info.sout

        return dict_mem
