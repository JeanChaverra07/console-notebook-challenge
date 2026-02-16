# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

class Note:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

def __init__(self, code: str, title: str, text: str, importance: str):
    self.code : str = code
    self.title : str = title
    self.text : str = text
