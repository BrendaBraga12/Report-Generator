from dataclasses import dataclass

@dataclass
class Product:
    id:str
    product_name:str
    company_name:str
    manufacturing_date:str
    expiration_date:str
    serial_number:str
    storage_instructions:str

    def __str__(self)->str:
        return f"The product {self.id} - {self.product_name}, with serial number {self.serial_number}, manufactured on {self.manufacturing_date}by the company {self.company_name}, valid until {self.expiration_date}, must be storage according to the following instructions:{self.storage_instructions}"
