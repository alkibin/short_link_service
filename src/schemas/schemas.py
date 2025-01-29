from pydantic import BaseModel


class Link(BaseModel):
    scheme: str
    netloc: str
    path: str | None = ''
    params: str | None = ''
    query: str | None = ''
    fragment: str | None = ''


class AddReturnString(Link):
    return_string: str