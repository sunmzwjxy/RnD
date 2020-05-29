# -- coding: utf-8 --

from CPU import cCPU
import SQL_DB

class cCPU_DB:
    def __init__(self,sql_DB,computer_ID = -1):
        self.m_DB = sql_DB
        self.m_computer_ID = computer_ID

    def process(self):
        cpu_times = cCPU().get_cpu_info(self.m_computer_ID)

        for itemlist in cpu_times:
            SQL = SQL_DB.get_i_sql("cpu",itemlist)
            self.m_DB.do_SQL_insert(SQL)

if __name__ == "__main__":
    cCPU_DB(None).process()

