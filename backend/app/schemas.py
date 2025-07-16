from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from datetime import datetime

class QuestionType(str, Enum):
    text = "text"
    single_choice = "single_choice"
    multiple_choice = "multiple_choice"

class OptionBase(BaseModel):
    text: str

class OptionCreate(OptionBase):
    pass

class OptionResponse(OptionBase):
    id: int
    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    text: str
    question_type: QuestionType

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    options: List[OptionResponse] = []
    class Config:
        orm_mode = True

class SurveyBase(BaseModel):
    title: str
    description: Optional[str] = None

class SurveyCreate(SurveyBase):
    pass

class SurveyResponse(SurveyBase):
    id: int
    created_at: datetime
    questions: List[QuestionResponse] = []
    class Config:
        orm_mode = True 