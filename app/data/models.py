from pydantic import BaseModel


class Body(BaseModel):
    word: str
    delimiters: list
