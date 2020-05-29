# -- coding: utf-8 --

import os
import sys
import configparser
#import MySQLdb
import pymysql

class CSQL_DB:
      def __init__(self):
            self.db = None
      
      def connect_DB(self):
            path = os.path.dirname(os.path.realpath(__file__)) + "\\config.ini"
            cf = configparser.ConfigParser()
            cf.read(path)
            #kvs = cf.items("db")
            self.db = pymysql.connect(host=cf.get("db","host"), port=cf.getint("db","port"), user=cf.get("db","user"), passwd=cf.get("db","passwd"), db=cf.get("db","db"))

      def do_SQL(self,sql):
            # 获取游标
            cursor = self.db.cursor()

            # SQL 
            # sql = "SELECT * FROM userinfo WHERE id = 1"

            try:
                  # do SQL
                  cursor.execute(sql)
                  # get result
                  results = cursor.fetchall()

                  return results
                  '''
                  for row in results:
                        fname = row[0]
                        lname = row[1]
                        age = row[2]
                        sex = row[3]
                        income = row[4]
                        print "fname=%d,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income )
                  '''
            except:
                  return None
                  # print "Error: unable to fecth data"

      def do_SQL_insert(self,sql):
            cursor = self.db.cursor()
            try:
                  cursor.execute(sql)
                  keyID = int(cursor.lastrowid)        #last ID
                  # return int(conn.insert_id()) # conn.insert_id() befor conn.commit() 
                  self.db.commit()

                  return keyID
            except Exception as err:
                  print (err.args)
                  self.db.rollback()
                  return None

      def disconnect_DB(self):
            self.db.close()

def safe(s):
      return pymysql.escape_string(s)

def get_i_sql(table, dict):
      '''
      生成insert的sql语句
      @table，插入记录的表名
      @dict,插入的数据，字典
      '''
      sql = 'insert into %s set ' % table
      sql += dict_2_str(dict)
      return sql


def get_s_sql(table, keys, conditions, isdistinct=0):
      '''
      生成select的sql语句
      @table，查询记录的表名
      @key，需要查询的字段
      @conditions,插入的数据，字典
      @isdistinct,查询的数据是否不重复
      '''
      if isdistinct:
            sql = 'select distinct %s ' % ",".join(keys)
      else:
            sql = 'select  %s ' % ",".join(keys)
      sql += ' from %s ' % table
      if conditions:
            sql += ' where %s ' % dict_2_str_and(conditions)
      return sql


def get_u_sql(table, value, conditions):
      '''
      生成update的sql语句
      @table，查询记录的表名
      @value，dict,需要更新的字段
      @conditions,插入的数据，字典
      '''
      sql = 'update %s set ' % table
      sql += dict_2_str(value)
      if conditions:
            sql += ' where %s ' % dict_2_str_and(conditions)
      return sql


def get_d_sql(table, conditions):
      '''
      生成detele的sql语句
      @table，查询记录的表名
      @conditions,插入的数据，字典
      '''
      sql = 'delete from  %s  ' % table
      if conditions:
            sql += ' where %s ' % dict_2_str_and(conditions)
      return sql


def dict_2_str(dictin):
      '''
      将字典变成，key='value',key='value' 的形式
      '''
      tmplist = []
      for k, v in dictin.items():
            tmp = "%s='%s'" % (str(k), safe(str(v)))
            tmplist.append(' ' + tmp + ' ')
      return ','.join(tmplist)


def dict_2_str_and(dictin):
      '''
      将字典变成，key='value' and key='value'的形式
      '''
      tmplist = []
      for k, v in dictin.items():
            tmp = "%s='%s'" % (str(k), safe(str(v)))
            tmplist.append(' ' + tmp + ' ')
      return ' and '.join(tmplist)