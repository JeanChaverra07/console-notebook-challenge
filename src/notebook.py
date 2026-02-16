# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

class Note:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

def __init__(self, code: str, title: str, text: str, importance: str):
    self.code : str = code
    self.title : str = title
    self.text : str = text
    self.importance : str = importance
    self.tags: list[str] = []

def add_tag(self, tag: str) -> None:
    if tag not in self.tags:
        self.tags.append(tag)

def __str__(self) -> str:
    tags_str = ', '.join(self.tags) if self.tags else ("No tags")
    return (
        f"Code: {self.code}\n"
        f"Title: {self.title}\n"
        f"Text: {self.text}\n"
        f"Importance: {self.importance}\n"
        f"Creation date: {self.creation_date}\n"
        f"Tags: {tags_str}"
    )