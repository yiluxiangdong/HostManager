#!/usr/bin/python
#-*- coding:utf-8 _*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import   pymysql

class SelectDB(object):
    def  __init__(self):
        self.conn = pymysql.connect(host='172.17.17.221', port=3306, user='root', passwd='111111', db='renting_test2', charset='utf8')
        self.cursor = self.conn.cursor()

    def  selectuser(self,name):
        if name:
            sql="SELECT id,mobile,name,id_card,renter_status  FROM  rms_renter WHERE  name LIKE CONCAT('%','{}','%')".format(name)
        else:
            sql = "SELECT id,mobile,name,id_card,renter_status  FROM  rms_renter"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return  data
        except Exception as e:
            print e
            return 0
    def updateuser(self,mobile,name,id_card,renter_status,id):
        if  id:
            sql = "UPDATE  rms_renter  SET mobile='{}',name='{}',id_card='{}',renter_status='{}' WHERE  id='{}'".format(mobile,name,id_card,renter_status,id)
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                return 1
            except Exception as e:
                print e
                return 0
        else:
            print 'update  error....'
            return 0


    def  selectHouse(self,name):
        name = str(name).strip()
        if name:
            sql="SELECT t.id, s.mobile,t.landlord_id,t.org_id,t.`name`,t.`status` FROM  rms_housing t  LEFT JOIN rms_landlord s ON s.id=t.landlord_id WHERE name   LIKE CONCAT('%','{}','%')".format(name)
        else:
            sql = "SELECT t.id, s.mobile,t.landlord_id,t.org_id,t.`name`,t.`status` FROM  rms_housing t  LEFT JOIN rms_landlord s ON s.id=t.landlord_id"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print e
            return 0



    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    result = SelectDB()
    # print  result.selectuser('车')
    # print  result.updateuser(u'18665333801', u'车谦1', u'440902198610220051', 4,99999)
    print result.selectHouse('中天')