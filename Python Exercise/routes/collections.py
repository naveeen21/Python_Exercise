from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Collection, EngagementPostCollection
from schemas import CreateCollectionRequest

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def create_collection(request: CreateCollectionRequest, db: Session = Depends(get_db)):
    collection = Collection(name=request.name)
    db.add(collection)
    db.commit()
    for post_id in request.post_ids:
        mapping = EngagementPostCollection(post_id=str(post_id), collection_id=collection.id, duration_in_seconds=0)
        db.add(mapping)
    db.commit()
    return {"message": "Collection created successfully", "collection_id": collection.id}
