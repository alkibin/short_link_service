from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse

from src.service.service import LinkService, get_link_service
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="/Users/aleksanderkibin/PycharmProjects/short_link_service/templates")

router = APIRouter(prefix='/link')


@router.post('/add')
async def process_link(link: str, service: LinkService = Depends(get_link_service)):
    short_link = await service.process_link(link)
    return {'short_link': short_link}


@router.get('/{short_link}')
async def redirect(short_link: str, service: LinkService = Depends(get_link_service)):
    original_url = await service.get_long_link(short_link)
    return RedirectResponse(url=original_url)

