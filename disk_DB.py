# -- coding: utf-8 --

from disk import cdisk
import SQL_DB

class cdisk_DB:
    def __init__(self,sql_DB,computer_ID):
        self.m_DB = sql_DB
        self.m_computer_ID = computer_ID

    def process(self):
        list_disk = cdisk().get_disk_info(self.m_computer_ID)

        for item in list_disk:
            SQL = SQL_DB.get_i_sql("disk",item)
            self.m_DB.do_SQL_insert(SQL)

if __name__ == "__main__":
    cdisk_DB(None,-1).process()