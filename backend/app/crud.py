from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status

# Encuesta
def create_survey(db: Session, survey: schemas.SurveyCreate):
    db_survey = models.Survey(title=survey.title, description=survey.description)
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

# Pregunta
def create_question(db: Session, survey_id: int, question: schemas.QuestionCreate):
    db_survey = db.query(models.Survey).filter(models.Survey.id == survey_id).first()
    if not db_survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    db_question = models.Question(text=question.text, question_type=question.question_type, survey_id=survey_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

# Opción
def create_option(db: Session, question_id: int, option: schemas.OptionCreate):
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    if db_question.question_type not in [models.QuestionType.single_choice, models.QuestionType.multiple_choice]:
        raise HTTPException(status_code=400, detail="Options only allowed for single_choice or multiple_choice questions")
    db_option = models.Option(text=option.text, question_id=question_id)
    db.add(db_option)
    db.commit()
    db.refresh(db_option)
    return db_option 