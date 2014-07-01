#coding=utf-8 
import sys
from socket import *
#serverHost = 'localhost'
serverHost = '42.91.187.183'
#42.91.187.183
#42.91.179.177
serverPort = 90

#Update Log:
#python作为Client端有协议的描述，但是Java作为Server端没有协议的定义
#两者可以连接上，python可以发数据到Java端，但是无法收到数据后显示在Client端
# socket.socket（协议,通讯方式） 创建socket对象  
# socket.AF_INET使用PIV4协议；  
# socket.SOCK_STREAM TCP通讯方式  
# socket.SOCK_DGTAM UDP通讯方式 

#host1 = gethostbyname("heyingyiran.vicp.cc") 用花生壳做一个域名映射，出现问题time out
#print host1
#serverHost=host1

#发送至服务端的默认文本
message = 'Hello world'
#如果参数大于1的话，连结的服务端为第一个参数
'''if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    #5如果参数大于2的话，连结的文字为第二个参数
    if len(sys.argv) > 2:
        message = sys.argv[2:]'''



sockobj = socket(AF_INET, SOCK_STREAM,0)
#连结至服务器及端口
sockobj.connect((serverHost, serverPort))

print 'Done'  
print 'Connecting to remote host...'   #到这一步可以建立连接
sockobj.send('北京会议\n')
print 'Data been sent'

data = sockobj.recv(2048)
#data=data.encode('utf-8')
    #确认他是引用的，是'x'
print 'Client received:',data
#关闭套接字
sockobj.close( )
