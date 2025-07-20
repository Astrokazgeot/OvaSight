from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import os
import uuid
import sys

from src.services.predict_services import predict_pcos
from src.database.operations import insert_patient, get_all_patients,get_patient_by_id
from src.exception import CustomException

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    name: str = Form(...),
    age: int = Form(...),
    bmi: float = Form(...)
):
    try:
        file_ext = file.filename.split('.')[-1].lower()
        if file_ext not in ["jpg", "jpeg", "png"]:
            raise HTTPException(status_code=400, detail="Unsupported file format. Please upload JPG or PNG.")

        
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.{file_ext}")
        with open(file_path, "wb") as f:
            f.write(await file.read())


        prediction_result, ovulation_status = predict_pcos(file_path)

        
        insert_patient(name, age, bmi, prediction_result, ovulation_status)

        return JSONResponse(content={
            "prediction": prediction_result,
            "ovulation_status": ovulation_status
        }, status_code=200)

    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(CustomException(e, sys)))

@router.get("/patients/{patient_id}")
async def get_patient_by_id_route(patient_id: int):
    try:
        patient = get_patient_by_id(patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")

        data = {
                "id": patient["id"],
                "name": patient["name"],
                "age": patient["age"],
                "bmi": patient["bmi"],
                "prediction_result": patient["prediction_result"],
                "ovulation_status": patient["ovulation_status"],
                "timestamp": patient["uploaded_at"].strftime("%Y-%m-%d %H:%M:%S")

        }

        return JSONResponse(content=data, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(CustomException(e, sys)))
