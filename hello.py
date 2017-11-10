#coding=utf-8
import sys
import MySQLdb


conn= MySQLdb.connect(
        host='rm-2zepysccz2h6p0h83o.mysql.rds.aliyuncs.com',
        port = 3306,
        user='yygk',
        passwd='Co185!*%',
        db ='yygk_core',
        )
cur = conn.cursor()
# SQL 更新语句
version = 2.99
content = 'test299'
sql = "update t_xt_xtcs set c_csz = %s WHERE c_csbm = %s "
val = ((version, 'wbglyapp_version'), (content, 'n_xbbgxnr_wbglyapp'))
print sql
try:
   # 执行SQL语句
   cur.executemany(sql, val)
   # 提交到数据库执行
   conn.commit()
   ret = "update success!\n"+ "version:" + str(version) +"\n" + "content:" + str(content)
except Exception, e:
   # 发生错误时回滚
   ret = e
   print e
   conn.rollback()

sys.exit(ret)
cur.close()
conn.commit()
conn.close()