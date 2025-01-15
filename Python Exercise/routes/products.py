from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import EngagementPostProduct
from schemas import CreateProductRequest

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def create_product(request: CreateProductRequest, db: Session = Depends(get_db)):
    product = EngagementPostProduct(name=request.name, image_url=request.image_url, sku=request.sku)
    db.add(product)
    db.commit()
    return {"message": "Product created successfully", "product_id": product.id}
