# -- coding: utf-8 --

from memory import cmemory
import SQL_DB

class cmemory_DB:
    def __init__(self,sql_DB,computer_ID):
        self.m_DB = sql_DB
        self.m_computer_ID = computer_ID

    def process(self):
        dict_mem = cmemory().get_mem_info(self.m_computer_ID)

        SQL = SQL_DB.get_i_sql("memory",dict_mem)
        self.m_DB.do_SQL_insert(SQL)