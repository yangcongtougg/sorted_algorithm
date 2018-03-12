# _*_ coding: utf-8 _*_
# @Time     :2018/3/8 15:09
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""
from socket import *

# tcp客户端已经连接好了服务器，以后的发送就不需要对方的ip个端口了
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('119.23.213.84',1234))
clientSocket.send()
#recvData = clientSocket.recv(1024)
#print('recvData: %s'%recvData)
clientSocket.close()