# -- coding: utf-8 --
import pymysql

class ConnectMySQL():
    def __init__(self) -> None:
        conn = pymysql.connect(host='localhost',user='root',password='root',database='testdemo')
        self.conn=conn
        #使用cursor()方法获取操作游标
        cursor=self.conn.cursor()
        self.cursor=cursor

    def executeSQL(self,sql):
        try:
            self.cursor.execute(sql)
            #接收全部的返回结果行
            results = self.cursor.fetchall()
            if len(results)>0:
                for row in results:
                    print(row)
            print('')
            self.conn.commit()
        except:
            #如果发生错误回滚
            self.conn.rollback()
        self.conn.close()


if __name__ == '__main__':
    insertsql='INSERT INTO newtable(name) values ("test")'
    selectSQL='select  name,email from t_system_user where name like "test%" '
    cm=ConnectMySQL()
    cm.executeSQL(selectSQL)