from abc import ABC,abstractmethod
import json
import csv
import sys
from product import Product


class Importer(ABC):
       def __init__(self,file_path:str):
        product1=Product("01","Farinha","Farinini","01-05-2021","02-06-2023","TY68 409C JJ43 AD1 PL2F","precisar ser armazenado em local protegido da luz.")


        @abstractmethod
        def import_data(self)->list[dict]:
         return Importer.__dict__
    

class JsonImporter(Importer):
       def __init__(self,file_path:str):
              self.file_path=file_path

@abstractmethod
def import_data(self)->list[dict]:
        with open(self.file_path,"r") as file:
               return json.load(file)   



class CsvImporters(Importer):
       def __ini__(self,id:str,product_name:str,company_name:str,manufacturing_date:str,expiration_date:str,serial_number:str,storage_instructions:str)->str:
           super().__init__(id,product_name,company_name,manufacturing_date,expiration_date,serial_number,storage_instructions)

@abstractmethod
def import_data(self)->list[dict]:
        with open("products.csv","r") as csv_file:
               csv_reader=csv.reader(csv_file)   


