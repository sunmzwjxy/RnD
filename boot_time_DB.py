# -- coding: utf-8 --

from boot_time import cboot_time
import SQL_DB

class cboot_time_DB:
    def __init__(self,sql_DB,computer_ID):
        self.m_DB = sql_DB
        self.m_computer_ID = computer_ID

    def process(self):
        boot_time = cboot_time().get_boot_time(self.m_computer_ID)

        SQL = SQL_DB.get_i_sql("boot_time",boot_time)
        self.m_DB.do_SQL_insert(SQL)