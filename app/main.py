import uvicorn
from fastapi import FastAPI
from app.api.v1 import survey as survey_router
from app.core.database import Base, engine

app = FastAPI(title="Student Survey Management – FastAPI")

# Routers
app.include_router(survey_router.router)

# Create tables automatically (Alembic is better in prod)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
