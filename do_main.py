# -- coding: utf-8 --

#import socket
from SQL_DB import CSQL_DB
from reboot_DB import creboot_DB
from platform_DB import cplatform_DB
from CPU_DB import cCPU_DB
from memory_DB import cmemory_DB
from disk_DB import cdisk_DB
from boot_time_DB import cboot_time_DB

class cdo_main:
    def __init__(self):
        self.my_DB = CSQL_DB()
   
    def do_DB(self):
        self.my_DB.connect_DB()

        # platform
        computerID = cplatform_DB(self.my_DB).process()
        # reboot
        creboot_DB(self.my_DB,computerID).process()
        # CPU
        cCPU_DB(self.my_DB,computerID).process()
        # memory
        cmemory_DB(self.my_DB,computerID).process()
        # disk
        cdisk_DB(self.my_DB,computerID).process()
        # boot time
        cboot_time_DB(self.my_DB,computerID).process()

        self.disconnect()
    
    def disconnect(self):
        self.my_DB.disconnect_DB()
