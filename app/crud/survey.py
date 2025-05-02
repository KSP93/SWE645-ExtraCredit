from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.survey import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate

async def get_all(db: AsyncSession):
    res = await db.execute(select(Survey))
    return res.scalars().all()

async def get_by_first_name(db: AsyncSession, name: str):
    res = await db.execute(select(Survey).where(Survey.first_name.ilike(f"%{name}%")))
    return res.scalars().all()

async def create(db: AsyncSession, payload: SurveyCreate):
    survey = Survey(**payload.model_dump())
    db.add(survey)
    await db.commit()
    await db.refresh(survey)
    return survey

async def update(db: AsyncSession, payload: SurveyUpdate):
    survey = await db.get(Survey, payload.id)
    if not survey:
        return None
    for k, v in payload.model_dump(exclude={"id"}).items():
        setattr(survey, k, v)
    await db.commit()
    await db.refresh(survey)
    return survey

async def delete(db: AsyncSession, survey_id: int):
    survey = await db.get(Survey, survey_id)
    if not survey:
        return False
    await db.delete(survey)
    await db.commit()
    return True
