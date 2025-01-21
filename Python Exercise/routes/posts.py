from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import EngagementPost

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{tenant_id}", response_model=dict)
def fetch_posts(tenant_id: str, db: Session = Depends(get_db)):
    posts = db.query(EngagementPost).filter(EngagementPost.tenant_id == tenant_id).all()
    return {"posts": posts}




