import mysql

class dataProduct:
    def loginVerify(self,user_name):
        sql = "select user_password from user_info where user_name = '%s'"%user_name
        result = mysql.DBMan().db_query(sql)[0][0]
        print result
        return result


    def drawBar(self,data):
        sql = "select product_name, sales from product"
        result = mysql.DBMan().db_query(sql)
        print result
        return result