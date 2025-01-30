from beanie import Document


class Link(Document):
    scheme: str
    netloc: str
    path: str
    params: str
    query: str
    fragment: str
    short_code: str | None = None
