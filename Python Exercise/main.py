from fastapi import FastAPI
from database import Base, engine
# from models import EngagementPost
from models import EngagementPost
from routes import products, collections, posts

# Initialize FastAPI app
app = FastAPI()

# Create database tables (ensure this runs without errors)
Base.metadata.create_all(bind=engine)

try:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")


# Include routers for different modules
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(collections.router, prefix="/collections", tags=["Collections"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])

# Ensure the app runs correctly and displays the Swagger UI
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application! Visit /docs for Swagger UI."}

