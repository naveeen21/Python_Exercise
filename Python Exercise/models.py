from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import uuid
from datetime import datetime

class EngagementPost(Base):
    __tablename__ = "engagement_post"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class EngagementPostContent(Base):
    __tablename__ = "engagement_post_content"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    post_id = Column(String, ForeignKey("engagement_post.id"), nullable=False)
    content_url = Column(String, nullable=False)

class EngagementPostProductMapping(Base):
    __tablename__ = "engagement_post_product_mapping"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    post_id = Column(String, ForeignKey("engagement_post.id"), nullable=False)
    product_id = Column(String, ForeignKey("engagement_post_product.id"), nullable=False)

class EngagementPostProduct(Base):
    __tablename__ = "engagement_post_product"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    sku = Column(String, nullable=False)

class Collection(Base):
    __tablename__ = "collection"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)

class EngagementPostCollection(Base):
    __tablename__ = "engagement_post_collection"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    post_id = Column(String, ForeignKey("engagement_post.id"), nullable=False)
    collection_id = Column(String, ForeignKey("collection.id"), nullable=False)
    duration_in_seconds = Column(Integer, nullable=False)
