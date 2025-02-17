from contextlib import asynccontextmanager

from fastapi import FastAPI


from app.database.database import createTables

from app.scheduler.main import scheduler

from fastapi.staticfiles import StaticFiles

from app.routers.main_sheet import router as main_sheet_router
from app.routers.products import router as products_router






@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await createTables()
    scheduler.start()
    yield



app = FastAPI(lifespan=lifespan)
app.mount('/static', app=StaticFiles(directory='static', html=True), name="static")
app.include_router(main_sheet_router)
app.include_router(products_router)