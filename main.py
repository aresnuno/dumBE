from fastapi import FastAPI
from api.routes.users import router as users_router
from api.routes.articles import router as articles_router
from database import engine
import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI MySQL Example",
    description="A simple FastAPI backend with MySQL",
    version="1.0.0"
)

# Include routers
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(articles_router, prefix="/articles", tags=["articles"])