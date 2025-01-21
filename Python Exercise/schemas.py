from pydantic import BaseModel, UUID4, HttpUrl
from typing import List

class CreateProductRequest(BaseModel):
    name: str
    image_url: HttpUrl
    sku: str

class CreateCollectionRequest(BaseModel):
    name: str
    post_ids: List[UUID4]