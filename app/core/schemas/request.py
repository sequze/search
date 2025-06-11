from pydantic import BaseModel


class RequestBase(BaseModel):
    name: str


class RequestRead(RequestBase):
    id: int
