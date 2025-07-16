from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/surveys", response_model=schemas.SurveyResponse, status_code=status.HTTP_201_CREATED)
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    return crud.create_survey(db, survey)

@router.post("/surveys/{survey_id}/questions", response_model=schemas.QuestionResponse, status_code=status.HTTP_201_CREATED)
def add_question(survey_id: int, question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db, survey_id, question)

@router.post("/questions/{question_id}/options", response_model=schemas.OptionResponse, status_code=status.HTTP_201_CREATED)
def add_option(question_id: int, option: schemas.OptionCreate, db: Session = Depends(get_db)):
    return crud.create_option(db, question_id, option) 