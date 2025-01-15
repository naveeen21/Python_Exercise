from fastapi import FastAPI
from database import Base, engine
from routes import products, collections, posts

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(collections.router, prefix="/collections", tags=["Collections"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
