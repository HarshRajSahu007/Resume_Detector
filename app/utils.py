import shutil
import os

def save_uploaded_file(file: UploadFile, upload_folder: str = "uploads"):
    """
    Save an uploaded file to the specified folder.
    """
    file_path = os.path.join(upload_folder, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_path