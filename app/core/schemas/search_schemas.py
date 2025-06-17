from pydantic import BaseModel
from typing import List


class SearchRequest(BaseModel):
    results: List[str]
    has_next: bool
