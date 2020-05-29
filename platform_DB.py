# -- coding: utf-8 --

from myplatform import cplatform
import SQL_DB

class cplatform_DB:
    def __init__(self,sql_DB):
        self.m_DB = sql_DB

    def process(self):
        computerID = -1
        m_platform = cplatform()
        dict_platf = m_platform.getplatform()

        SQL = SQL_DB.get_s_sql("computer","*",{"IP":dict_platf["IP"]})

        result = self.m_DB.do_SQL(SQL)
        if len(result) != 0:  # find
            for item in result:
                computerID = item[0]
        else:   # not find
            SQL = SQL_DB.get_i_sql("computer",dict_platf)
            computerID = self.m_DB.do_SQL_insert(SQL)

        return computerID