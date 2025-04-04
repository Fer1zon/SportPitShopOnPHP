from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/catalog")

templates = Jinja2Templates(directory="templates")

@router.get("")
async def get_catalog(request : Request):
    return templates.TemplateResponse(request, "catalog.html")
    
