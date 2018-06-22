# _*_ coding:utf-8 _*_
from socket import *
from threading import Thread
import re

HTML_ROOT_DIR = "./html"

class HTTPServer(object):
    """"""
    def __init__(self):
        # 1.创建套接字
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 3.监听套接字,主动转被动

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_addr = self.server_socket.accept()
            # 4.创建一个处理客户端的线程
            client_deal = Thread(target=self.client_handle, args=(client_socket, client_addr))
            # 5.开启线程
            client_deal.start()
            # 6.不能关闭套接字

    def start_response(self, status, headers):
        """
         status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    star
        """
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header

        self.response_headers = response_headers

    def client_handle(self,client_socket,client_addr):
        print("[%s]客户端已连接" % str(client_addr))
        # 获得客户端的请求数据
        request_data = client_socket.recv(1024)
        request_lines = request_data.decode("gb2312").splitlines()
        # 分行打印请求信息
        for line in request_lines:
            print(line)
        request_start_line = request_lines[0]
        # 测试检查请求头
        print("request_start_line:", request_start_line)

        # 解析请求头
        # GET / HTTP / 1.1
        # 使用正则表达式提取出链接中文件的地址
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line).group(1)
        print(file_name)
        method = re.match(r"(\w+) +/[^ ]* ",request_start_line).group(1)

        # /ctime.py
        if file_name.endswith(".py"):
            try:
                m = __import__(file_name[1:-3])
            except Exception:
                self.response_headers = "HTTP/1.1 404 Not Found\r\n"
                response_body = "not found"
            else:
                env = {
                    "PATH_INFO": file_name,
                    "METHOD": method
                }

                response_body = m.application(env, self.start_response)

            response_data = self.response_headers + "\r\n" + response_body
        else:
            if "/" == file_name:
                file_name = "/index.html"
            # 打开服务器中的文件，并读取出来
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 如果服务器没有这个文件，就回应一个错误
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_headers = "Server: My Server\r\n"
                response_body = "The file is not found\r\n"
            else:
                # print("*"*10)
                # print(file_name)
                file_data = file.read()
                file.close()
                # 构造返回客户端response数据
                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_headers = "Server: Jack Server\r\n"
                response_body = file_data.decode("utf-8")

            response_data = response_start_line + response_headers + "\r\n" + response_body
            print("response:", response_data)
        # 向客户端发送数据
        client_socket.send(response_data.encode("gb2312"))
        # 注意：在主函数可不加关闭套接字，但在一个进程或线程中必须使用完要关闭
        # 否则，网络通信时会认为数据没有发送完毕
        client_socket.close()
    def bind(self,port):
        self.server_socket.bind(("192.168.155.2",port))


def main():
    http_server = HTTPServer()
    # http_server.set_port()
    http_server.bind(7788)
    http_server.start()
    http_server.client_handle()

if __name__ == "__main__":
    main()