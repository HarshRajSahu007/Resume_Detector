from sqlalchemy.orm import Session
from .models import Resume

def create_resume(db: Session, resume_data: dict):
    """
    Create a new resume entry in the database.
    """
    resume = Resume(
        name=resume_data["name"],
        skills=resume_data["skills"],
        experience=resume_data["experience"],
        education=resume_data["education"],
    )
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume