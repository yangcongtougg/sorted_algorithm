# _*_ coding: utf-8 _*_
# @Time     :2018/3/8 14:34
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
"""

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 1234))
serverSocket.listen(5)  # 同时监听5人,套接字创建默认是主动的，listen将主动改为被动。
print('serverScoket处于堵塞状态，等待别人接入')
newSocket, clientAddr = serverSocket.accept()
print('有人接入，新的socket返回')
# newSocket表示这个新客户端真正负责传输数据的套接字
# clientAddr表示这个客户端的ip及port，理解10086总台（监听套接字）及之下的客服服务流程，10086空出。
recvData = newSocket.recv(1024)
print('通话开始')
print('%s: %s' % (str(clientAddr), recvData))
newSocket.close()
serverSocket.close()
