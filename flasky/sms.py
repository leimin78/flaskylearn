#coding:utf-8


import time
from subprocess import *


# """ 显示当前时间"""
nowtime = time.strftime('%Y-%m-%d %H:%M',time.localtime())
today = time.strftime('%Y%m%d')
sqltime = time.strftime('%Y%m%d%H%M')+'00'
f1 = open('/home/oracle/leimin/sms_report/total_subscribe.txt','r')
f2 = open('/home/oracle/leimin/sms_report/new_subscribe.txt','r')
f3 = open('/home/oracle/leimin/sms_report/new_unsubscribe.txt','r')

total = f1.readline().strip()
newsub = f2.readline().strip()
newunsub = f3.readline().strip()

if total =='':
    total = 0
if newsub == '':
    newsub = 0
if newunsub == '':
    newunsub = 0

f1.close()
f2.close()
f3.close()
"""
insert into com_bgt_sm_20170328(bs_file_id, bs_service_code, bs_content, bs_time, bs_src_id, bs_receiver_num) values(99999999, 13, 'content', '20170328100000', '160', '1157842914');
"""


def createSql(receivers):
    #邮件正文
    content = """
Now Time is: %s
Still now the total subscribe is: %s
Today new subscribes is: %s
Today new unsubribes is: %s """ % (nowtime,total,newsub,newunsub)

    for receiver in receivers:
        p = Popen('sqlplus csmaindb/huawei123',stdin=PIPE,shell=True)
        sql = """
insert into com_bgt_sm_%s(bs_file_id, bs_service_code, bs_content, bs_time, bs_src_id, bs_receiver_num) values(99999999,13,'%s','%s','160','%s');
commit;
    """ %(today,content,sqltime,receiver)
        p.stdin.write(sql)
        print sql



if __name__ == '__main__':
    receivers = ['1157842914']
    createSql(receivers)
