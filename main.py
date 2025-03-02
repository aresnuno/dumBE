from fastapi import FastAPI, File, UploadFile
from api.routes.users import router as users_router
from api.routes.articles import router as articles_router
from fastapi.middleware.cors import CORSMiddleware
import models
# In a Python script or FastAPI startup
from database import engine, Base
import shutil
import os


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI MySQL Example",
    description="A simple FastAPI backend with MySQL",
    version="1.0.0"
)
origins = [
    "http://localhost:3000",  # Nuxt.js frontend
    "http://127.0.0.1:3000",  # Alternative for local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ✅ Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # ✅ Allow all headers
)


# Include routers
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(articles_router, prefix="/articles", tags=["articles"])
UPLOAD_DIR = "uploads"

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"url": f"http://localhost:8000/{file_location}"}

# Mount the uploads directory to serve files
from fastapi.staticfiles import StaticFiles
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")