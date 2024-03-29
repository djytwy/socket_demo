# !/usr/bin/env python
# encoding: utf-8

"""
file: socket_server.py
time: 2019/7/8 13:47
Author: twy
contact: 19983195362
des:
"""

# 创建服务器用到的模块
import socketserver


class MySelfServer(socketserver.BaseRequestHandler):  # 第一步创建一个自己的server类，继承BaseRequestHandler类

    # 重写BaseRequestHandler类中的handle方法，直接写在自己创建的类中就可以了
    def handle(self):  # 里面的内容为服务器端跟客户端的所有交互

        # 接收数据
        data = self.request.recv(1024).strip()

        # 打印客户端ip地址和发送来的数据，这里可能会问为什么会有self.client_address这个参数，这个在父类构造函数中
        print("{} wrote:".format(self.client_address[0]))
        # self.request.sendall('yuuii')
        print(data)

        # 判断客户端是否断开
        if not data:
            print(self.client_address, '的链接断开了！')  # 等待接收但接收为空则客户端断开

        # 将接收到的数据大写发送回去
        # self.request.sendall(data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # 第二步实例化四个类其中之一并传入服务器地址和上面自己创建的服务器类，这里自己实例化的TCPServer
    server = socketserver.TCPServer((HOST, PORT), MySelfServer)

    # 处理多个请求，这里注意的是虽然是处理多个请求，但是这句话并没有实现并发
    server.serve_forever()
