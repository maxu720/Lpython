import socket
import multiprocessing


class Server_Http(object):
    def __init__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", 9999))
        server_socket.listen(128)
        self.server_socket = server_socket
    def Server_web(self,client_socket):
        self.client_socket = client_socket
        client_data = client_socket.recv(4096)
        if not client_data:
            print("客户端已经关闭")
            client_socket.close()
            return

        client_str_data = client_data.decode()
        client_line = client_str_data.split("\r\n")[0]
        path_info = client_line.split(" ")[1]
        print(path_info)
        if path_info == '/':
            path_info = '/index.html'
        try:
            with open("./static" + path_info, "rb") as file:
                file_data = file.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_headr = "s\ServerPython2.0\r\n"
            response_body = "404 Not Found"
            response_data = response_line + response_headr + "\r\n" + response_body
            client_socket.send(response_data.encode())
        else:
            response_line = "HTTP/1.1 200 ok\r\n"
            response_headr = "s\ServerPython2.0\r\n"
            response_body = file_data
            response_data = (response_line + response_headr + "\r\n").encode() + response_body
            client_socket.send(response_data)
        finally:
            client_socket.close()
    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print("收到%s的请求" % str(client_addr))
            pro = multiprocessing.Process(target=self.Server_web, args=(client_socket,))
            pro.start()
            client_socket.close()

if __name__ == '__main__':
   server = Server_Http()
   server.start()