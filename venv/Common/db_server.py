
import pymysql
import os
import sys
from Common.config import YamlOperation
sys.path.append(os.getcwd())
os.chdir(os.path.abspath('..') + '/Data')

data = YamlOperation(os.getcwd() + "\data.yaml")

class DbMysql(object):

    def __init__(self,dbinfo):
        self.db = pymysql.connect(
            cursorclass=pymysql.cursors.DictCursor,
            **dbinfo
        )

        # 创建游标
        self.cursor = self.db.cursor()

    def select(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self,sql):
        '''执行（增、删、改）'''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    mysql_info =data.DB
    db = DbMysql(mysql_info)
   #test sql
    inv_email = '"' + data.Invitaion__bus_email.email1 + data.Email_type.snapmail + '"'
    operation_email='"' + data.Bussiness_acc.Admin_email + '"'


    sql  = 'SELECT * FROM invitation_account WHERE email='+inv_email;
    print(sql)
    result = db.select(sql)
    print(result)
    db.close()
