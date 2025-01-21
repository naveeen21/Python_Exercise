from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import EngagementPostProduct
from schemas import CreateProductRequest

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(request: CreateProductRequest, db: Session = Depends(get_db)):
    # Create a new product
    new_product = EngagementPostProduct(
        name=request.name,
        image_url=request.image_url,
        sku=request.sku
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {"message": "Product created successfully", "product": {
        "id": new_product.id,
        "name": new_product.name,
        "image_url": new_product.image_url,
        "sku": new_product.sku
    }}
 




