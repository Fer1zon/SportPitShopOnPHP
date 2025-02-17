from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import SCHEDULER_DATABASE_URL

scheduler = AsyncIOScheduler(
{
    
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': SCHEDULER_DATABASE_URL
    }
})#, timezone="Europe/Moscow",







