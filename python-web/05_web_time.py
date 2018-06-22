import time


def application(env, start_response):

    # 状态码
    status = "200 OK"
    # 响应头
    headers = {
        ("Content-Type", "text/html")
    }
    # 接收状态码和响应报头
    start_response(status, headers)
    return time.ctime()