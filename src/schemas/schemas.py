from pydantic import BaseModel


class LinkModel(BaseModel):
    scheme: str
    netloc: str
    path: str | None = ''
    params: str | None = ''
    query: str | None = ''
    fragment: str | None = ''
    short_code: str | None = None

