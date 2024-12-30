from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv() 

# Initialize the FastAPI app
app = FastAPI()

# Load environment variables (if any)
UPLOAD_DIR = os.getenv('UPLOAD_DIR', './app/uploads')
UPLOAD_DIR = os.path.abspath(UPLOAD_DIR)  

# Ensure the upload directory exists
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

# Create a route for file upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Generate a unique filename to prevent overwriting
        file_extension = file.filename.split('.')[-1]
        unique_filename = f"{uuid4().hex}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        # Save the uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Return a success message with the file path
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully", "file_path": file_path})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")
