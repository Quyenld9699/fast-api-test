from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import postes, user

app = FastAPI(
    title="TestAppFastAPI",
    description="App này làm ra với mục đích học FastAPI",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Le Dinh Quyen",
        "url": "https://github.com/Quyenld9699",
        "email": "quyenld9699@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3333",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(postes.router)
app.include_router(user.router)

# Get - for testing
@app.get("/", tags=["test"])
def greet():
    return {"message": "Em chào anh Quyền ạ!"}



