from typing import Dict

class HttpRequest:
    def __init__(self, body: Dict=None, parametro: Dict=None) -> None:
        self.body = body 
        self.parametro = parametro