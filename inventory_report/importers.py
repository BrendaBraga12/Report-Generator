from abc import ABC,abstractmethod
import json
import csv
import sys
from inventory_report.product import Product


class Importer(ABC):
       def __init__(self,path:str)->None:
              self.path=path

       @abstractmethod
       def import_data(self)->list[Product]:
              return NotImplementedError("Esse é um método abstrato."
                                         "Deve ser implementados nas classes filhas")
    

class JsonImporter(Importer):
       def __init__(self,path:str):
              super().__init__(path)

       
       def import_data(self):
        products=[]
        with open(self.path,"r") as file:
               item=json.load(file)
               for product in item:
                     product1=Product(*product.values())
                     products.append(product1)
        return products

class CsvImporter(Importer):
       def __init__(self,path:str)->str:
           super().__init__(path)

       
       def import_data(self):
        products=[]
        with open(self.path,"r") as csv_file:
               csv_reader=csv.DictReader(csv_file)
               for product in csv_reader:
                   product1=Product(*product.values())
                   products.append(product1)          
        return products

