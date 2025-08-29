from report import Report
from inventory_report.inventory import Inventory
from datetime import date


class SimpleReport():
   

 def add_inventory(self,inventory:Inventory):
    self.Reports.append(Report)


def generate(self)->str:
    closestdate=""
    maior=""
    FabricacaoAntiga=""
    if date.today("YYYY-MM-DD")<=self.expiration_date("YYYY-MM-DD"):
        for c in range(0,len(Report)):
            if c==0:
             FabricacaoAntiga=self.manufacturing_date[0]
            elif FabricacaoAntiga<self.manufacturing_date[c]:
             FabricacaoAntiga=self.manufacturing_date[c]

        for c in range(0,len(Report)):
            if c==0:
                closestdate=self.expiration_date("YYYY-MM-DD")
            elif self.expiration_date("YYYY-MM-DD")<closestdate:
                closestdate=self.expiration_date("YYYY-MM-DD")

        for c in range (0,len(Report)):
            if c==0:
                 maior=sum(len(Report[c]))
            elif sum(len(Report[c]))>maior:
                maior=self.company_name

        
    return f"""Oldest manufacturing date:{FabricacaoAntiga}
               Closest expiration date:{closestdate}
               Company with the largest inventory:{self.company_name}"""
        