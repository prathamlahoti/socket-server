import settings
import socket
from typing import Tuple, Dict
from views import index, post

# All available routes for a client to get HTML-content
ROUTES: Dict[str, callable] = {
    '/': index,
    '/post': post,
}


def handle_request(request: str) -> Tuple[str, str]:
    """ Splitting request on request METHOD and request ROUTE

        :param request: user request data, sent to the server
        :returns user: request method and its route
    """
    method, route = request.split(' ')[0:2]
    return method, route


def generate_headers(method: str, route: str) -> Tuple[str, int]:
    """ Generates headers to be sent with server response

        :param method: user request method to the server
        :param route: user route, addressed to the server
        :returns: HTTP-headers and HTTP-status code, depending on user request method and route
     """
    if route not in ROUTES:
        return settings.HEADERS[404], settings.HTTP_STATUS_CODES[404]

    if not method == 'GET':
        return settings.HEADERS[405], settings.HTTP_STATUS_CODES[405]

    return settings.HEADERS[200], settings.HTTP_STATUS_CODES[200]


def generate_message(http_status_code: int, route: str) -> str:
    """ Generates a message to be sent to a user request

        :param http_status_code: user request http-status code
        :param route: user request route, addressed to the server

        :returns: HTML-view, if user route is in ROUTES, otherwise - http-error message
     """
    if http_status_code == settings.HTTP_STATUS_CODES[404]:
        return settings.HTTP_STATUS_MESSAGES[404]

    if http_status_code == settings.HTTP_STATUS_CODES[405]:
        return settings.HTTP_STATUS_MESSAGES[405]

    return ROUTES[route]()


def generate_response(request: str) -> bytes:
    """ Compacts headers and message for a user request to be sent to a user as a server response

        :param request: user request, sent to the server
        :returns: Encoded response to a user

     """
    method, route = handle_request(request)
    headers, http_status_code = generate_headers(method, route)
    response = headers + generate_message(http_status_code, route)
    return response.encode()


def server_run():
    """ Creates server socket and handles user request to the server """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Setting socket flags and activating it
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Connecting our socket with specified host and port
        server_socket.bind((settings.SOCKET_HOST, settings.SOCKET_PORT))
        # Waiting for requests to the socket
        server_socket.listen(1)
        while True:
            # Creating client socket
            client_socket, addr = server_socket.accept()
            # receiving data from the socket
            data = client_socket.recv(1024)
            if not data:
                break

            # Displaying the server state in console
            print(data, '\n', addr, '\n')
            # Request from the browser is obtained in bytes, so we need to decode it
            response = generate_response(data.decode('utf-8'))
            # Sending response to a user and closing connection
            client_socket.sendall(response)
            client_socket.close()


if __name__ == "__main__":
    server_run()
