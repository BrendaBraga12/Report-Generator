from typing import Optional

class Inventory():
       total_active_tasks=0
       def __init__(self,data,tasks:Optional[list[str]]=None):
              self.data=data
              self.tasks=tasks if tasks else[]
              self.increase_amount_of_tasks(len(self.tasks))

def add_data(self,task:str):
       self.tasks.append(task)
       self.increase_amount_task()