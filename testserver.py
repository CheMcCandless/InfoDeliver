#socket server端
#获取socket构造及常量
from socket import *
#''代表服务器为localhost
myHost = ''
#在一个非保留端口号上进行监听
myPort = 90

#设置一个TCP socket对象
sockobj = socket(AF_INET, SOCK_STREAM)
#绑定它至端口号
sockobj.bind((myHost, myPort))
#监听，允许5个连结
sockobj.listen(5)

#直到进程结束时才结束循环
while True:
    #等待下一个客户端连结
    connection, address = sockobj.accept( )
    #连结是一个新的socket
    print 'Server connected by', address
    while True:
        #读取客户端套接字的下一行
        data = connection.recv(1024)
        #data为从作为client的python后台接受到的原始数据，java进行发送给腾讯服务器后获得返回数据
        #如果没有数量的话，那么跳出循环
        if not data: break
        #发送一个回复至客户端
    
        connection.send('After Analyzed：20C')
    #当socket关闭时eof
    connection.close( )
