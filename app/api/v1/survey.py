from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.survey import SurveyRead, SurveyCreate, SurveyUpdate
from app.crud import survey as crud

router = APIRouter(prefix="/api/surveys", tags=["surveys"])

@router.get("", response_model=List[SurveyRead])
async def list_surveys(db: AsyncSession = Depends(get_db)):
    return await crud.get_all(db)

@router.get("/search", response_model=List[SurveyRead])
async def search_surveys(name: str, db: AsyncSession = Depends(get_db)):
    return await crud.get_by_first_name(db, name)

@router.post("/create", response_model=SurveyRead, status_code=status.HTTP_201_CREATED)
async def create_survey(payload: SurveyCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.post("/update", response_model=SurveyRead)
async def update_survey(payload: SurveyUpdate, db: AsyncSession = Depends(get_db)):
    updated = await crud.update(db, payload)
    if not updated:
        raise HTTPException(404, "Survey not found")
    return updated

@router.post("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_survey(id: int, db: AsyncSession = Depends(get_db)):
    ok = await crud.delete(db, id)
    if not ok:
        raise HTTPException(404, "Survey not found")
