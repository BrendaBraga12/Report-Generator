from typing import Optional
from inventory_report.product import Product

class Inventory():
       total_active_tasks = 0
       def __init__(self,data:Optional[list[Product]]=None)->None:
              self.data=[] if data is None else data

       def add_data(self,data:list[Product]):
              self.data.extend(data)
