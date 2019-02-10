from typing import Dict

SOCKET_HOST: str = '127.0.0.1'
SOCKET_PORT: int = 50007

HTTP_STATUS_CODES: Dict[int, int] = {
    404: 404,
    405: 405,
    200: 200,
}

HTTP_STATUS_MESSAGES: Dict[int, str] = {
    404: '404 Page Not Found\n',
    405: 'Method Not Allowed\n',
}

HEADERS: Dict[int, str] = {
    404: 'HTTP/1.1 404 Not found\n\n',
    405: 'HTTP/1.1 405 Method not allowed\n\n',
    200: 'HTTP/1.1 200 OK\n\n',
}

