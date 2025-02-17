from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.database.models import Model
from config import DATABASE_URL
dbEngine = create_async_engine(DATABASE_URL)


new_session = async_sessionmaker(dbEngine, class_ = AsyncSession, expire_on_commit=False)
async def createTables():
    async with dbEngine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)