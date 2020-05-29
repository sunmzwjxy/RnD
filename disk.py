# -- coding: utf-8 --

import psutil

class cdisk:
    def __init__(self):
        pass

    def get_disk_info(self,computer_ID):
        list_disk = []
        for id in psutil.disk_partitions():
            if 'cdrom' in id.opts or id.fstype == '':
                continue
            #disk_name = id.device.split(':')
            disk_info = psutil.disk_usage(id.device)
            list_disk.append({"computer_ID":computer_ID,"name":id.device,
            "fstype":id.fstype,"total":disk_info.total,"used":disk_info.used,
            "free":disk_info.free,"percent":disk_info.percent})

        return list_disk