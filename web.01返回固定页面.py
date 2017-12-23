# import socket
# def Server_web(client_socket):
#     client_data = client_socket.recv(4096)
#     if not client_data:
#         print("客户端已经关闭")
#         client_socket.close()
#         return
#     response_line = "HTTP/1.1 200 ok\r\n"
#     response_headr = "s\ServerPython1.0\r\n"
#     response_body = "hello python"
#     response_data = response_line + response_headr + "\r\n" +response_body
#     client_socket.send(response_data.encode())
#     client_socket.close()
#
# if __name__ == '__main__':
#     server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     server_socket.bind(("",9999))
#     server_socket.listen(128)
#     while True:
#         client_socket, client_addr = server_socket.accept()
#         print("收到%s的请求" % str(client_addr))
#         Server_web(client_socket)





