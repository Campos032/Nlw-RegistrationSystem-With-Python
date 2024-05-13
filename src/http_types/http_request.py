from typing import Dict

class HttpResponse:
    def __init__(self, body: Dict=None, parametro: Dict=None) -> None:
        self.body = body 
        self.parametro = parametro