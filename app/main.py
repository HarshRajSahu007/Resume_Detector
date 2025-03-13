from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from .nlp import extract_entities
from .ocr import extract_text_from_pdf, extract_text_with_tesseract
from .crud import create_resume
from .models import Base, SessionLocal, engine
from .utils import save_uploaded_file

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = save_uploaded_file(file)

    # Extract text from the file
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_with_tesseract(file_path)

    # Extract entities
    entities = extract_entities(text)

    # Save to database
    db = SessionLocal()
    resume_data = {
        "name": " ".join(entities["NAME"]),
        "skills": entities["SKILLS"],
        "experience": entities["EXPERIENCE"],
        "education": entities["EDUCATION"],
    }
    create_resume(db, resume_data)

    return JSONResponse(content=entities)
    


        