import socket
import pymysql
from jinja2 import Template

def foo(request):
    f = open("静态页面/login.html", "rb")
    data = f.read()
    f.close()
    return data

def var(request):
    f = open("静态页面/userinfo.html", "rb")
    data = f.read()
    f.close()
    return data

def f3(request):

    conn = pymysql.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "123",
        database = "ssm",
        charset = "utf8"
    )

    cursor = conn.cursor()
    sql = "select id,name,email from users"
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()

    userinfo = []
    for item in res:
        tp = "<tr>"\
             "<td>%s</td>" \
             "<td>%s</td>" \
             "<td>%s</td>" \
             "</tr>"%(item[0], item[1], item[2])
        userinfo.append(tp)
    s = "".join(userinfo)

    f = open("静态页面/userinfo.html", mode="r", encoding="utf-8")
    data = f.read()
    f.close()

    data = data.replace("@@sss@@", s)
    return bytes(data, encoding="utf-8")

def f4(request):

    conn = pymysql.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "123",
        database = "ssm",
        charset = "utf8"
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select id,name,email from users"
    cursor.execute(sql)
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('静态页面/hostlist.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()

    # 使用第三方工具实现模板渲染
    template = Template(data)
    data = template.render(xxxx=user_list,sus='nihao')
    return bytes(data, encoding='utf-8')


routers = [
    ("/xxx", foo),
    ("/xxx?username=123&pwd=123&submit=%E6%8F%90%E4%BA%A4", var),
    ("/sss", f3),
    ("/yyy", f4)
]

# web 服务
def run():
    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 解决重复启动时,会报Address already in use错误问题
    sk.bind(("localhost", 8080))
    sk.listen(5)

    while True:
        conn,addr = sk.accept()
        data = conn.recv(8096) #接收浏览器发送的请求头
        data_str = str(data, encoding="utf-8")
        headers,bodys = data_str.split("\r\n\r\n")
        temp_list = headers.split("\r\n")
        method,url,protocal = temp_list[0].split(" ")

        conn.send(b"HTTP/1.1 200 OK\r\n\r\n") #回应响应头
        func_name = None
        print("--->" + str(routers))
        for item in routers:
            print("--->item0" + str(item[0]))
            print("--->url" + url)
            if item[0] == url:
                print("===>" + str(item))
                func_name = item[1]
                break


        if func_name:
            res = func_name(data_str)
        else:
            res = b"404"

        conn.send(res) #回应响应体 (网页主体文本内容)
        conn.close()

if __name__ == '__main__':
    run()
