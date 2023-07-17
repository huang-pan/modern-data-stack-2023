from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request

router = APIRouter(
  prefix='/dependencies',
  tags=['dependencies']
)

def convert_headers(request: Request, separator: str = '--'):
  out_headers = []
  for key, value in request.headers.items():
    out_headers.append(f"{key} {separator} {value}")
  return out_headers

@router.get('')
def get_items(separator: str = '--', headers = Depends(convert_headers)):
  return {
    'items': ['a', 'b', 'c'],
    'headers': headers
  }

@router.post('/new')
def create_item(headers = Depends(convert_headers)):
  return {
    'result': 'new item created',
    'headers': headers
  }