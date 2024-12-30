from fastapi import APIRouter, UploadFile, File
from typing import List
from fastapi.responses import JSONResponse

router = APIRouter()

# Route for uploading files
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Logic for saving the uploaded file
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return JSONResponse(content={"message": "File uploaded successfully", "file_location": file_location})

# You can add other routes here (for example, for processing the file, etc.)
