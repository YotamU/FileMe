import socket
import re
import codecs
import threading
import django

print_lock = threading.Lock()

def func():
    # Define socket host and port
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000


    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print('Listening on port %s ...' % SERVER_PORT)


    HTTP_OK = "HTTP/1.1 200 OK\r\n"
    ACC = "Accept:text/html\r\n"
    CONTENT_LENGTH = "Content-Length:"
    CONTENT_HTML = "Content-Type: text/html; charset=utf-8\r\n"
    CONTENT_IMAGE = "Content-Type: image/jpeg\r\n"
    CONTENT_GIF = "Content-type: image/gif"
    HTTP_error = "HTTP/1.0 404 Not Found"
    client_connection, client_address = server_socket.accept()

    while True:
        # Get the client request
        request = client_connection.recv(1024).decode()
        request_split = request.split('\n', 1)[0]
        if "GET" in request_split or "HEAD" in request_split:
            result = re.search('GET (.*) HTTP', request_split)
            if result.group(1) == "/":
                    # Send INDEX response
                    HTML_WEB = codecs.open("Index.html", 'r').read()
                    index = str(HTTP_OK + CONTENT_HTML + ACC + "\r\n" + HTML_WEB)
                    client_connection.send(index.encode())
        request = client_connection.recv(1024).decode()
        if not request:
            print_lock.release()
            break
func()
