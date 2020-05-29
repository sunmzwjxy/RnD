# -- coding: utf-8 --

import datetime
from reboot import creboot
import SQL_DB

class creboot_DB:
    def __init__(self,sql_DB,computer_ID = -1):
        self.m_DB = sql_DB
        self.m_computer_ID = computer_ID

    def isfirstdayofcurrentmonth(self):
        cur = datetime.datetime.now()
        time = datetime.date(cur.year,cur.month,cur.day)
        first_day = datetime.date(time.year, time.month, 1)
        if time == first_day:
            return True
        else:
            return False
    
    def process(self):
        #if self.isfirstdayofcurrentmonth() == True:        #只在每月的1号执行
        m_do = creboot(self.m_computer_ID)
        m_do.getAllEvents(None, ["System"], "C:\\Temp")

        for item in m_do.list_event:
            SQL = SQL_DB.get_i_sql("reboot",item)
            newindex = self.m_DB.do_SQL_insert(SQL)
