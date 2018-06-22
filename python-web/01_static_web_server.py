#_*_ code:utf-8 _*_

from socket import *
from multiprocessing import Process

def client_deal(client_socket):

    """ 处理客户端的请求 """

    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print(request_data.decode("utf-8"))

    #构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server:my server\r\n"
    responce_body = "hello itcast"
    response = response_start_line + response_headers + "\r\n" + responce_body
    print("response:",response)

    #向客户端返回响应数据
    #client_socket.send(bytes(response,"utf-8"))
    client_socket.send(response.encode("utf-8"))

    #关闭客户端连接（套接字）
    client_socket.close()


def main():
    # tcpsocket 服务端
    HTML_ROOT_DIR = "" #路径
    tcp_server = socket(AF_INET, SOCK_STREAM)  # 使用internet网的地址协议
    local_addr = ("", 7788)
    tcp_server.bind(local_addr)
    tcp_server.listen(128)

    while True:
        client_socket, client_info = tcp_server.accept()
        print("[%s]客户端已连接" % str(client_info))
        client_deal_process = Process(target=client_deal,args=(client_socket,))
        client_deal_process.start()
        client_socket.close()#因为子进程已经把父进程的所有信息都copy了一份，故此处可关闭
                            #但如果是在多线程当中，因为多线程是共用一个套接字，关闭可导致信息收发产生问题


if __name__ == "__main__":
    main()



