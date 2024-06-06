from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Set, Dict
from datetime import datetime

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: Set[str] = set()
item = Item(name='Coffee', price=2.5, description='Freshly brewed coffee', tags={'Beverage', 'Breakfast'})
custom_encoders = {datetime: lambda v: v.strftime('%Y-%m-%d')}
json_compatible_item_data = jsonable_encoder(item,  {'name', 'description', 'price'}, exclude={'tax'})
