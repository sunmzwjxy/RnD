# -- coding: utf-8 --

import psutil
import datetime

class cboot_time:
    def __init__(self):
        pass

    def get_boot_time(self,computer_ID):
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

        return {"computer_ID":computer_ID,"time":boot_time}
