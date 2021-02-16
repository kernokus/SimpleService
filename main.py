import socket
from views import *

# URLS - список возможных адресов
URLS = {
    '/': mainPage,
    '/second': secondPage
}


def parse_request(request):  # возвращает метод и url, на который обратился клиент
    parsed_list = request.split(' ')
    return parsed_list[0], parsed_list[1]


def generate_headers(method, url):
    if not method == 'GET':
        return 'HTTP/1.1 405 Method not allowed\n\n', 405
    if not url in URLS:
        return 'HTTP/1.1 404 Not found\n\n', 404
    return 'HTTP/1.1 200 OK\n\n', 200


def generate_content(code, url):  # возвращает контент в ответ на запрос клиента
    if code == 404:
        return '<h1>code 404</h1>'
    if code == 405:
        return '<h1>method not allowed - 405</h1>'
    return URLS[url]()  # для вызова функции в словаре URLS


def generate_response(request):  # генерирует ответ на запрос клиента
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()  # получаем сокет пользователя
        request = client_socket.recv(1024)  # получил инф-ю
        print('request' + str(request))
        print()
        print('адрес' + str(addr))

        response = generate_response(request.decode('utf-8'))
        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
