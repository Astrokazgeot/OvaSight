from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router
from src.exception import CustomException

app = FastAPI(
    title="OvaSight - PCOS Detection API",
    description="Upload ultrasound + personal data to predict PCOS and ovulation status.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/")
def read_root():
    try:
        return {"message": "Welcome to OvaSight PCOS Detection API"}
    except Exception as e:
        raise CustomException(f"Error in root endpoint: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
